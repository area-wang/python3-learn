from fastapi import APIRouter, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.deps import CommentDep, CurrentUser, PostDep, SessionDep
from app.exceptions import PermissionDeniedError
from app.models import Comment
from app.schemas.comment import CommentCreate, CommentOut

router = APIRouter(tags=["comments"])


@router.get("/posts/{post_id}/comments", response_model=list[CommentOut])
def list_comments(post: PostDep, session: SessionDep) -> list[Comment]:
    return list(
        session.scalars(
            select(Comment)
            .where(Comment.post_id == post.id)
            .options(selectinload(Comment.author))
            .order_by(Comment.id)
        )
    )


@router.post(
    "/posts/{post_id}/comments",
    response_model=CommentOut,
    status_code=status.HTTP_201_CREATED,
)
def create_comment(
    comment_in: CommentCreate, post: PostDep, current_user: CurrentUser, session: SessionDep
) -> Comment:
    comment = Comment(content=comment_in.content, post=post, author=current_user)
    session.add(comment)
    session.commit()
    return comment


@router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment: CommentDep, current_user: CurrentUser, session: SessionDep) -> None:
    # 评论作者本人或文章作者都可以删除评论
    if current_user.id not in (comment.author_id, comment.post.author_id):
        raise PermissionDeniedError("只能删除自己的评论或自己文章下的评论")
    session.delete(comment)
    session.commit()
