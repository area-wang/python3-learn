from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Page(BaseModel, Generic[T]):
    """通用分页响应：Page[PostOut]、Page[UserPublic] ……"""

    items: list[T]
    total: int
    page: int
    size: int
    pages: int


class ErrorInfo(BaseModel):
    code: str
    message: str
    details: list[dict[str, Any]] | None = None


class ErrorResponse(BaseModel):
    """所有错误响应的统一结构，只用于 OpenAPI 文档展示（responses={...: {"model": ErrorResponse}}）。"""

    error: ErrorInfo
    request_id: str | None = None
