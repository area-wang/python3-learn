from pathlib import Path
from typing import Annotated
from uuid import uuid4
from fastapi import FastAPI, File, Form, Header, HTTPException, UploadFile,  status, Request

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_TYPES= {"image/png": ".png", "image/jpg": ".jpg"}
API_KEY="secret123"

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(
    x_api_key: Annotated[str, Header()],
    title: Annotated[str, Form(min_length=1, max_length=50)],
    images: Annotated[list[UploadFile], File()],
    user_agent: Annotated[str | None, Header()] = None
):
    if x_api_key != API_KEY:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "API key 无效")
    saved = []
    for image in images:
        suffix = ALLOWED_TYPES.get(image.content_type)
        if suffix is None:
            raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, f"不支持的文件类型： {image.content_type}")

        dest = UPLOAD_DIR / f"{uuid4().hex}{suffix}"
        dest.write_bytes(await image.read())
        saved.append({"original": image.filename, "stored": dest.name})
    return {"title": title, "images": saved, "client": user_agent}