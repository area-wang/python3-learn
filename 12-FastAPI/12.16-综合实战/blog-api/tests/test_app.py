def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "database": "ok"}


def test_request_id_and_timing_headers(client):
    resp = client.get("/health", headers={"X-Request-ID": "my-trace-id"})
    assert resp.headers["X-Request-ID"] == "my-trace-id"
    assert resp.headers["X-Process-Time"].endswith("ms")

    generated = client.get("/health").headers["X-Request-ID"]
    assert len(generated) == 32


def test_request_id_in_error_body(client):
    resp = client.get("/posts/999", headers={"X-Request-ID": "trace-404"})
    assert resp.json()["request_id"] == "trace-404"


def test_unknown_route_uses_unified_error(client):
    resp = client.get("/no-such-route")
    assert resp.status_code == 404
    assert resp.json()["error"]["code"] == "NOT_FOUND"


def test_method_not_allowed(client):
    resp = client.put("/health")
    assert resp.status_code == 405
    assert resp.json()["error"]["code"] == "METHOD_NOT_ALLOWED"


def test_cors_preflight(client):
    resp = client.options(
        "/posts",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "POST",
        },
    )
    assert resp.status_code == 200
    assert resp.headers["access-control-allow-origin"] == "http://localhost:5173"


def test_openapi_schema(client):
    schema = client.get("/openapi.json").json()
    assert "/posts/{post_id}" in schema["paths"]
    assert "OAuth2PasswordBearer" in schema["components"]["securitySchemes"]
