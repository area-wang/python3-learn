from datetime import timedelta

from app.core.security import create_access_token


def test_register_returns_user_without_password(client):
    resp = client.post(
        "/auth/register",
        json={"username": "alice", "email": "alice@example.com", "password": "password123"},
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["username"] == "alice"
    assert body["email"] == "alice@example.com"
    assert "password" not in body and "hashed_password" not in body


def test_register_duplicate_username_returns_409(client, register):
    register("alice")
    resp = client.post(
        "/auth/register",
        json={"username": "alice", "email": "other@example.com", "password": "password123"},
    )
    assert resp.status_code == 409
    assert resp.json()["error"]["code"] == "CONFLICT"


def test_register_validation_error_has_unified_format(client):
    resp = client.post(
        "/auth/register",
        json={"username": "a!", "email": "not-an-email", "password": "short"},
    )
    assert resp.status_code == 422
    body = resp.json()
    assert body["error"]["code"] == "VALIDATION_ERROR"
    fields = {d["field"] for d in body["error"]["details"]}
    assert fields == {"body.username", "body.email", "body.password"}
    assert body["request_id"]


def test_login_success(client, register):
    register("alice")
    resp = client.post("/auth/token", data={"username": "alice", "password": "password123"})
    assert resp.status_code == 200
    assert resp.json()["token_type"] == "bearer"


def test_login_wrong_password(client, register):
    register("alice")
    resp = client.post("/auth/token", data={"username": "alice", "password": "wrong-pass"})
    assert resp.status_code == 401
    assert resp.headers["WWW-Authenticate"] == "Bearer"
    assert resp.json()["error"]["code"] == "UNAUTHORIZED"


def test_login_unknown_user(client):
    resp = client.post("/auth/token", data={"username": "nobody", "password": "password123"})
    assert resp.status_code == 401


def test_me_requires_token(client):
    resp = client.get("/users/me")
    assert resp.status_code == 401
    assert resp.json()["error"]["code"] == "UNAUTHORIZED"


def test_me_with_invalid_token(client):
    resp = client.get("/users/me", headers={"Authorization": "Bearer not-a-jwt"})
    assert resp.status_code == 401


def test_me_with_expired_token(client, register):
    user = register("alice")
    token = create_access_token(user["id"], expires_delta=timedelta(seconds=-1))
    resp = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 401


def test_me_and_update_me(client, alice):
    resp = client.get("/users/me", headers=alice)
    assert resp.status_code == 200
    assert resp.json()["username"] == "alice"

    resp = client.patch("/users/me", json={"bio": "热爱 Python"}, headers=alice)
    assert resp.status_code == 200
    assert resp.json()["bio"] == "热爱 Python"


def test_change_password(client, alice, login):
    resp = client.patch("/users/me", json={"password": "new-password"}, headers=alice)
    assert resp.status_code == 200
    login("alice", "new-password")  # 新密码能登录


def test_public_profile_hides_email(client, register):
    user = register("alice")
    resp = client.get(f"/users/{user['id']}")
    assert resp.status_code == 200
    assert "email" not in resp.json()
