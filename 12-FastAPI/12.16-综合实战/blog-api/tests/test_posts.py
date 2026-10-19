def test_create_post_normalizes_tags(client, alice, create_post):
    post = create_post(alice, title="Hello", tags=[" Python ", "python", "FastAPI", ""])
    assert post["tags"] == ["python", "fastapi"]
    assert post["author"]["username"] == "alice"


def test_create_post_requires_auth(client):
    resp = client.post("/posts", json={"title": "t", "content": "c"})
    assert resp.status_code == 401


def test_create_post_validation(client, alice):
    resp = client.post("/posts", json={"title": "", "content": "c"}, headers=alice)
    assert resp.status_code == 422
    assert resp.json()["error"]["details"][0]["field"] == "body.title"


def test_too_many_tags(client, alice):
    resp = client.post(
        "/posts",
        json={"title": "t", "content": "c", "tags": ["a", "b", "c", "d", "e", "f"]},
        headers=alice,
    )
    assert resp.status_code == 422


def test_get_post_detail(client, alice, create_post):
    post = create_post(alice)
    resp = client.get(f"/posts/{post['id']}")
    assert resp.status_code == 200
    assert resp.json()["comments"] == []


def test_get_missing_post_returns_404(client):
    resp = client.get("/posts/999")
    assert resp.status_code == 404
    assert resp.json()["error"] == {
        "code": "NOT_FOUND",
        "message": "文章 999 不存在",
        "details": None,
    }


def test_pagination(client, alice, create_post):
    for i in range(15):
        create_post(alice, title=f"post-{i}")

    first = client.get("/posts", params={"page": 1, "size": 10}).json()
    assert first["total"] == 15
    assert first["pages"] == 2
    assert len(first["items"]) == 10
    assert first["items"][0]["title"] == "post-14"  # 最新的在前

    second = client.get("/posts", params={"page": 2, "size": 10}).json()
    assert len(second["items"]) == 5


def test_pagination_limits(client):
    assert client.get("/posts", params={"size": 1000}).status_code == 422
    assert client.get("/posts", params={"page": 0}).status_code == 422


def test_unknown_query_param_rejected(client):
    resp = client.get("/posts", params={"pgae": 2})
    assert resp.status_code == 422


def test_search_and_filters(client, alice, bob, create_post):
    create_post(alice, title="学习 FastAPI", tags=["python"])
    create_post(alice, title="Rust 入门", content="所有权", tags=["rust"])
    create_post(bob, title="FastAPI 部署", tags=["python", "devops"])

    def titles(**params):
        return sorted(p["title"] for p in client.get("/posts", params=params).json()["items"])

    assert titles(q="fastapi") == ["FastAPI 部署", "学习 FastAPI"]
    assert titles(q="所有权") == ["Rust 入门"]
    assert titles(tag="Python") == ["FastAPI 部署", "学习 FastAPI"]
    bob_id = client.get("/users/me", headers=bob).json()["id"]
    assert titles(author_id=bob_id) == ["FastAPI 部署"]


def test_author_can_update(client, alice, create_post):
    post = create_post(alice, tags=["old"])
    resp = client.patch(
        f"/posts/{post['id']}", json={"title": "新标题", "tags": ["new"]}, headers=alice
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["title"] == "新标题"
    assert body["content"] == post["content"]  # 未传的字段保持不变
    assert body["tags"] == ["new"]


def test_other_user_cannot_update_or_delete(client, alice, bob, create_post):
    post = create_post(alice)
    resp = client.patch(f"/posts/{post['id']}", json={"title": "hack"}, headers=bob)
    assert resp.status_code == 403
    assert resp.json()["error"]["code"] == "FORBIDDEN"
    assert client.delete(f"/posts/{post['id']}", headers=bob).status_code == 403


def test_update_order_401_before_404(client):
    # 未登录访问不存在的文章：先报 401 而不是 404，避免泄露资源是否存在
    assert client.patch("/posts/999", json={"title": "x"}).status_code == 401


def test_author_can_delete(client, alice, create_post):
    post = create_post(alice)
    resp = client.delete(f"/posts/{post['id']}", headers=alice)
    assert resp.status_code == 204
    assert resp.content == b""
    assert client.get(f"/posts/{post['id']}").status_code == 404


def test_timestamps_are_utc_aware(client, alice, create_post):
    created = create_post(alice)
    listed = client.get("/posts").json()["items"][0]
    # 新建返回和查询返回格式一致，都带时区
    assert created["created_at"].endswith("Z")
    assert listed["created_at"] == created["created_at"]
