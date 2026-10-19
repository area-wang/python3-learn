import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.core.config import get_settings
from app.core.middleware import request_context_middleware
from app.db import engine, init_db
from app.deps import SessionDep
from app.exceptions import register_exception_handlers
from app.routers import auth, comments, posts, users

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
logger = logging.getLogger("blog")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # 启动：建表（真实项目通常交给 Alembic 迁移，这里为了开箱即用）
    init_db()
    logger.info("数据库已就绪：%s", engine.url.render_as_string(hide_password=True))
    yield
    # 关闭：释放连接池
    engine.dispose()
    logger.info("应用已关闭")


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="FastAPI 综合实战：用户、文章、标签、评论与 JWT 认证。",
        lifespan=lifespan,
    )

    # 中间件：后添加的在外层。请求先经过 request_context_middleware，再经过 CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Request-ID", "X-Process-Time"],
    )
    app.middleware("http")(request_context_middleware)

    register_exception_handlers(app)

    app.include_router(auth.router)
    app.include_router(users.router)
    app.include_router(posts.router)
    app.include_router(comments.router)

    @app.get("/health", tags=["health"])
    def health(session: SessionDep) -> dict[str, str]:
        session.execute(text("SELECT 1"))
        return {"status": "ok", "database": "ok"}

    return app


app = create_app()
