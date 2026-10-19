import math
from typing import Annotated

from fastapi import APIRouter, Query, status
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from app.deps import CurrentUser, OwnPostDep, SessionDep
from app.exceptions import NotFoundError
from app.models import Comment, Post, Tag
from app.schemas.common import ErrorResponse, Page
from app.schemas.post import PostCreate, PostDetail, PostFilter, PostOut, PostUpdate

router = APIRouter(prefix="/posts", tags=["posts"])

AUTH_RESPONSES = {
    401: {"model": ErrorResponse, "description": "未登录或令牌无效"},
    403: {"model": ErrorResponse, "description": "不是文章作者"},
    404: {"model": ErrorResponse, "description": "文章不存在"},
}


def get_or_create_tags(session: Session, names: list[str]) -> list[Tag]:
    """已有的标签复用，没有的新建（随文章一起 commit）。"""
    if not names:
        return []
    existing = session.scalars(select(Tag).where(Tag.name.in_(names))).all()
    by_name = {tag.name: tag for tag in existing}
    return [by_name.get(name) or Tag(name=name) for name in names]


@router.get("", response_model=Page[PostOut])
def list_posts(filters: Annotated[PostFilter, Query()], session: SessionDep) -> Page[PostOut]:
    stmt = select(Post)
    if filters.q:
        pattern = f"%{filters.q}%"
        stmt = stmt.where(or_(Post.title.ilike(pattern), Post.content.ilike(pattern)))
    if filters.tag:
        stmt = stmt.where(Post.tags.any(Tag.name == filters.tag.strip().lower()))
    if filters.author_id is not None:
        stmt = stmt.where(Post.author_id == filters.author_id)

    total = session.scalar(select(func.count()).select_from(stmt.subquery())) or 0

    posts = session.scalars(
        stmt.options(
            # 一次性批量加载所有文章的作者和标签，避免 N+1 查询
            selectinload(Post.author),
            selectinload(Post.tags),
        )
        .order_by(Post.created_at.desc(), Post.id.desc())
        .offset((filters.page - 1) * filters.size)
        .limit(filters.size)
    ).all()

    return Page[PostOut](
        items=[PostOut.model_validate(post) for post in posts],
        total=total,
        page=filters.page,
        size=filters.size,
        pages=math.ceil(total / filters.size),
    )


@router.post(
    "",
    response_model=PostOut,
    status_code=status.HTTP_201_CREATED,
    responses={401: AUTH_RESPONSES[401]},
)
def create_post(post_in: PostCreate, current_user: CurrentUser, session: SessionDep) -> Post:
    post = Post(
        title=post_in.title,
        content=post_in.content,
        author=current_user,
        tags=get_or_create_tags(session, post_in.tags),
    )
    session.add(post)
    session.commit()
    return post


@router.get("/{post_id}", response_model=PostDetail, responses={404: AUTH_RESPONSES[404]})
def get_post(post_id: int, session: SessionDep) -> Post:
    post = session.scalar(
        select(Post)
        .where(Post.id == post_id)
        .options(
            selectinload(Post.author),
            selectinload(Post.tags),
            # 链式 selectinload：评论 + 每条评论的作者
            selectinload(Post.comments).selectinload(Comment.author),
        )
    )
    if post is None:
        raise NotFoundError(f"文章 {post_id} 不存在")
    return post


@router.patch("/{post_id}", response_model=PostOut, responses=AUTH_RESPONSES)
def update_post(post_in: PostUpdate, post: OwnPostDep, session: SessionDep) -> Post:
    # exclude_unset：没传的字段不动；exclude_none：显式传 null 也忽略（这些列都不允许为空）
    data = post_in.model_dump(exclude_unset=True, exclude_none=True)
    if "tags" in data:
        post.tags = get_or_create_tags(session, data.pop("tags"))
    for field, value in data.items():
        setattr(post, field, value)
    session.commit()
    return post


@router.delete(
    "/{post_id}", status_code=status.HTTP_204_NO_CONTENT, responses=AUTH_RESPONSES
)
def delete_post(post: OwnPostDep, session: SessionDep) -> None:
    session.delete(post)  # 评论通过 cascade="all, delete-orphan" 一起删除
    session.commit()
