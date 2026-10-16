from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary = "hello wordl", description="测试接口")
async def read_root():
    return {"Hello": "World"}