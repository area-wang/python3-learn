from typing import Annotated
from pathlib import Path

import aiofiles
import aiofiles.os
from fastapi import FastAPI, Form, File, UploadFile, HTTPException, status
import shutil

app = FastAPI()

@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form(min_length=6)]
):
    return {"username": username}

@app.post("/files")
async def save_file(
    file: UploadFile
):
    print(file)
    content = await file.read()
    return {"file": file, "content": len(content)}

UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
CHUNK_SIZE=1024 * 1024
MAX_SIZE= 1024 * 1024 * 5

@app.post("/upload")
async def upload(file: UploadFile):
    dest = UPLOAD_DIR / Path(file.filename).name
    size = 0
    with dest.open("wb") as f:
        while chunk:= await file.read(CHUNK_SIZE):
            size+=len(chunk)
            if size > MAX_SIZE:
                f.close()
                dest.unlink()
                raise HTTPException(status.HTTP_413_CONTENT_TOO_LARGE, "文件过大")
            f.write(chunk)
    return {"filename": file.filename, "saved_to": str(dest), "size": size}


@app.post("/upload-async")
async def upload_async(file: UploadFile):
    dest = UPLOAD_DIR / Path(file.filename).name
    size = 0
    async with aiofiles.open(dest, "wb") as f:
        while chunk := await file.read(CHUNK_SIZE):
            size += len(chunk)
            if size > MAX_SIZE:
                break
            await f.write(chunk)
    # 退出 async with 后文件已关闭，再删除
    if size > MAX_SIZE:
        await aiofiles.os.remove(dest)
        raise HTTPException(status.HTTP_413_CONTENT_TOO_LARGE, "文件过大")
    return {"filename": file.filename, "saved_to": str(dest), "size": size}

@app.post("/upload-sync")
def upload_sync(file: UploadFile):
    dest = UPLOAD_DIR / Path(file.filename).name
    with dest.open("wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"saved_to": str(dest), "file_type": type(file.file).__name__}


@app.post("/multi")
async def multi(files: Annotated[list[UploadFile], File(description="上传多个文件")]):
    return {"names": [file.filename for file in files], "count": len(files)}

