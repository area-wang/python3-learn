from fastapi import APIRouter
from sqlalchemy import select

from app.core.security import hash_password
from app.deps import CurrentUser, SessionDep
from app.exceptions import ConflictError, NotFoundError
from app.models import User
from app.schemas.user import UserOut, UserPublic, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
def read_me(current_user: CurrentUser) -> User:
    return current_user


@router.patch("/me", response_model=UserOut)
def update_me(user_in: UserUpdate, current_user: CurrentUser, session: SessionDep) -> User:
    data = user_in.model_dump(exclude_unset=True, exclude_none=True)

    if "email" in data and data["email"] != current_user.email:
        taken = session.scalar(select(User).where(User.email == data["email"]))
        if taken is not None:
            raise ConflictError("邮箱已被占用")
    if "password" in data:
        current_user.hashed_password = hash_password(data.pop("password"))

    for field, value in data.items():
        setattr(current_user, field, value)
    session.commit()
    return current_user


# 注意：/me 必须定义在 /{user_id} 之前，否则 "me" 会先被当成 user_id 匹配（然后 422）
@router.get("/{user_id}", response_model=UserPublic)
def read_user(user_id: int, session: SessionDep) -> User:
    user = session.get(User, user_id)
    if user is None:
        raise NotFoundError(f"用户 {user_id} 不存在")
    return user
