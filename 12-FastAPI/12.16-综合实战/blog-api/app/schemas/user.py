from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=32, pattern=r"^[A-Za-z0-9_]+$")
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    bio: str | None = Field(default=None, max_length=500)
    password: str | None = Field(default=None, min_length=8, max_length=128)


class UserPublic(BaseModel):
    """对外公开的用户信息（文章作者、评论作者），不含邮箱。"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    bio: str


class UserOut(UserPublic):
    """用户本人可见的信息。注意：永远不包含 hashed_password。"""

    email: EmailStr
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
