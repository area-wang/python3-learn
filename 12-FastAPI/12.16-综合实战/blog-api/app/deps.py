from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.db import get_db
from app.exceptions import AuthenticationError, NotFoundError, PermissionDeniedError
from app.models import Comment, Post, User

# ---------- 数据库 ----------

SessionDep = Annotated[Session, Depends(get_db)]

# ---------- 认证 ----------

# tokenUrl 只用于 /docs 页面的 Authorize 按钮，告诉它去哪里换 token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
TokenDep = Annotated[str, Depends(oauth2_scheme)]


def get_current_user(session: SessionDep, token: TokenDep) -> User:
    user_id = decode_access_token(token)
    if user_id is None or not user_id.isdigit():
        raise AuthenticationError("无效或已过期的令牌")
    user = session.get(User, int(user_id))
    if user is None or not user.is_active:
        raise AuthenticationError("用户不存在或已被禁用")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]

# ---------- 资源加载 + 权限 ----------
# 把「查不到就 404」「不是作者就 403」做成依赖，路由函数里只剩业务逻辑


def get_post_or_404(post_id: int, session: SessionDep) -> Post:
    post = session.get(Post, post_id)
    if post is None:
        raise NotFoundError(f"文章 {post_id} 不存在")
    return post


PostDep = Annotated[Post, Depends(get_post_or_404)]


def get_own_post(user: CurrentUser, post: PostDep) -> Post:
    # 参数顺序决定依赖求值顺序：先认证（401），再查文章（404），最后判权限（403）
    if post.author_id != user.id:
        raise PermissionDeniedError("只能修改或删除自己的文章")
    return post


OwnPostDep = Annotated[Post, Depends(get_own_post)]


def get_comment_or_404(comment_id: int, session: SessionDep) -> Comment:
    comment = session.get(Comment, comment_id)
    if comment is None:
        raise NotFoundError(f"评论 {comment_id} 不存在")
    return comment


CommentDep = Annotated[Comment, Depends(get_comment_or_404)]
