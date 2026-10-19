from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import or_, select

from app.core.security import DUMMY_HASH, create_access_token, hash_password, verify_password
from app.deps import SessionDep
from app.exceptions import AuthenticationError, ConflictError
from app.models import User
from app.schemas.common import ErrorResponse
from app.schemas.user import Token, UserCreate, UserOut

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    responses={409: {"model": ErrorResponse, "description": "用户名或邮箱已被注册"}},
)
def register(user_in: UserCreate, session: SessionDep) -> User:
    exists = session.scalar(
        select(User).where(or_(User.username == user_in.username, User.email == user_in.email))
    )
    if exists is not None:
        raise ConflictError("用户名或邮箱已被注册")

    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hash_password(user_in.password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.post(
    "/token",
    response_model=Token,
    responses={401: {"model": ErrorResponse, "description": "用户名或密码错误"}},
)
def login(
    form: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep,
) -> Token:
    """OAuth2 密码流：表单字段 username / password（application/x-www-form-urlencoded）。"""
    user = session.scalar(select(User).where(User.username == form.username))
    if user is None:
        verify_password(form.password, DUMMY_HASH)  # 消除时序差异
        raise AuthenticationError("用户名或密码错误")
    if not verify_password(form.password, user.hashed_password):
        raise AuthenticationError("用户名或密码错误")
    if not user.is_active:
        raise AuthenticationError("账号已被禁用")
    return Token(access_token=create_access_token(user.id))
