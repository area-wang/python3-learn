from collections.abc import Iterator
from datetime import datetime, timezone

from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.types import TypeDecorator

from app.core.config import get_settings

settings = get_settings()

# SQLite 默认禁止跨线程复用连接，而 FastAPI 会把同步路由/依赖放到线程池执行，所以要关掉检查
connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}

engine = create_engine(settings.database_url, connect_args=connect_args, echo=settings.debug)

# expire_on_commit=False：commit 后对象属性不过期，返回给 response_model 序列化时不会再触发查询
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class UTCDateTime(TypeDecorator[datetime]):
    """统一按 UTC 存取的时间类型。

    SQLite 不保存时区信息，读回来是 naive datetime；这里读出时补上 UTC，
    保证接口返回的时间始终带时区（JSON 里以 Z 结尾），新建和查询结果格式一致。
    """

    impl = DateTime(timezone=True)
    cache_ok = True

    def process_result_value(self, value: datetime | None, dialect) -> datetime | None:
        if value is not None and value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value


def get_db() -> Iterator[Session]:
    """每个请求一个 Session，请求结束（包括抛异常）时自动关闭。"""
    with SessionLocal() as session:
        yield session


def init_db() -> None:
    # 导入 models 包，确保所有模型类都注册到了 Base.metadata 上
    from app import models  # noqa: F401

    Base.metadata.create_all(bind=engine)
