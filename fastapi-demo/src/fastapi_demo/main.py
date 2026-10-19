from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import Annotated
from pydantic import AfterValidator

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet="resnet"
    lenet="lenet"

app = FastAPI(
    title="商品服务",
    description="一个用于学习的FastAPI的示例服务",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json"
)



fake_db: dict[int, dict] = {1:{"name": "键盘"}, 2: {"name":"鼠标"}}

def check(value:str)->str:
    if not value.startswith(("isa_", "isb_")):
        raise ValueError('必须以isa_ 或者isb_ 开头')
    return value


@app.get("/items")
async def list_items():
    return list(fake_db.values())

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return fake_db.get(item_id)

@app.post("/items",
    status_code=201,
    tags=["items"],
    summary="创建商品"
)
async def create_item(name:str):
    new_id = max(fake_db) + 1
    fake_db[new_id] = {"name": name}
    return {"id": new_id, "name": name}

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id:int):
    fake_db.pop(item_id, None)

@app.api_route("/order", methods=["GET", "POST"])
async def order(orderId:int):
    return {"orderId": orderId, "amount": 123}

@app.get("/file/{file_path:path}")
async def get_file(file_path: str):
    return {"file": file_path}

@app.get("/search")
async def search(
    q: Annotated[str, Query(min_length=3, max_length=10, pattern="^[a-z]+$")],
    page: Annotated[int, Query(ge=1)] =1
):
    return {"q":q, "page":page}

@app.get("/test/{id}")
async def get_id(
  id: Annotated[int, Path(ge=1)]
):
    return {"id": id}

@app.get("/check")
async def check(
    c: Annotated[str | None, AfterValidator(check)] = None
):
    return {"c": c}