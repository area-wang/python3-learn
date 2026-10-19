from datetime import datetime
from typing import Annotated, Any

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, field_validator

from app.schemas.comment import CommentOut
from app.schemas.user import UserPublic

MAX_TAG_LENGTH = 30


def normalize_tags(tags: list[str]) -> list[str]:
    """去空白、转小写、去重（保持顺序），并检查长度。"""
    result: list[str] = []
    for raw in tags:
        tag = raw.strip().lower()
        if not tag:
            continue
        if len(tag) > MAX_TAG_LENGTH:
            raise ValueError(f"标签长度不能超过 {MAX_TAG_LENGTH} 个字符：{tag!r}")
        if tag not in result:
            result.append(tag)
    return result


# 可复用的「标签列表」类型：最多 5 个，校验通过后自动规范化
TagList = Annotated[list[str], Field(max_length=5), AfterValidator(normalize_tags)]


class PostCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1)
    tags: TagList = []


class PostUpdate(BaseModel):
    """PATCH 用：所有字段可选，只更新客户端真正传了的字段。"""

    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None, min_length=1)
    tags: TagList | None = None


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    tags: list[str]
    author: UserPublic
    created_at: datetime
    updated_at: datetime

    @field_validator("tags", mode="before")
    @classmethod
    def tag_objects_to_names(cls, value: Any) -> Any:
        # ORM 里 post.tags 是 Tag 对象列表，对外只暴露标签名
        return [getattr(tag, "name", tag) for tag in value]


class PostDetail(PostOut):
    comments: list[CommentOut]


class PostFilter(BaseModel):
    """列表查询参数模型：在路由里写成 Annotated[PostFilter, Query()]。"""

    model_config = ConfigDict(extra="forbid")  # 传了未知查询参数直接 422，避免拼写错误被静默忽略

    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    q: str | None = Field(default=None, max_length=100, description="在标题和正文中搜索")
    tag: str | None = None
    author_id: int | None = None
