import os

# 必须在导入 app 之前设置：app/db.py 在导入时就会根据配置创建 engine
os.environ["BLOG_DATABASE_URL"] = "sqlite://"
os.environ["BLOG_SECRET_KEY"] = "test-secret-key-at-least-32-bytes-long"

from collections.abc import Callable, Iterator  # noqa: E402

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy import create_engine  # noqa: E402
from sqlalchemy.orm import Session, sessionmaker  # noqa: E402
from sqlalchemy.pool import StaticPool  # noqa: E402

from app.db import Base, get_db  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture
def session_factory() -> Iterator[sessionmaker[Session]]:
    # 内存 SQLite + StaticPool：所有连接共用同一个底层连接，
    # 否则每个新连接都会看到一个全新的空数据库
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    yield sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture
def client(session_factory: sessionmaker[Session]) -> Iterator[TestClient]:
    def override_get_db() -> Iterator[Session]:
        with session_factory() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:  # with 会触发 lifespan
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def register(client: TestClient) -> Callable[..., dict]:
    def _register(username: str, password: str = "password123", email: str | None = None) -> dict:
        resp = client.post(
            "/auth/register",
            json={"username": username, "email": email or f"{username}@example.com", "password": password},
        )
        assert resp.status_code == 201, resp.text
        return resp.json()

    return _register


@pytest.fixture
def login(client: TestClient) -> Callable[..., dict[str, str]]:
    def _login(username: str, password: str = "password123") -> dict[str, str]:
        resp = client.post("/auth/token", data={"username": username, "password": password})
        assert resp.status_code == 200, resp.text
        return {"Authorization": f"Bearer {resp.json()['access_token']}"}

    return _login


@pytest.fixture
def alice(register, login) -> dict[str, str]:
    """已注册并登录的用户 alice，返回认证请求头。"""
    register("alice")
    return login("alice")


@pytest.fixture
def bob(register, login) -> dict[str, str]:
    register("bob")
    return login("bob")


@pytest.fixture
def create_post(client: TestClient) -> Callable[..., dict]:
    def _create(headers: dict[str, str], **fields) -> dict:
        payload = {"title": "标题", "content": "正文内容", "tags": []} | fields
        resp = client.post("/posts", json=payload, headers=headers)
        assert resp.status_code == 201, resp.text
        return resp.json()

    return _create
