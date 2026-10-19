def test_add_and_list_comments(client, alice, bob, create_post):
    post = create_post(alice)
    resp = client.post(f"/posts/{post['id']}/comments", json={"content": "写得好"}, headers=bob)
    assert resp.status_code == 201
    assert resp.json()["author"]["username"] == "bob"

    comments = client.get(f"/posts/{post['id']}/comments").json()
    assert [c["content"] for c in comments] == ["写得好"]

    detail = client.get(f"/posts/{post['id']}").json()
    assert detail["comments"][0]["author"]["username"] == "bob"


def test_comment_on_missing_post(client, alice):
    resp = client.post("/posts/999/comments", json={"content": "hi"}, headers=alice)
    assert resp.status_code == 404


def test_empty_comment_rejected(client, alice, create_post):
    post = create_post(alice)
    resp = client.post(f"/posts/{post['id']}/comments", json={"content": ""}, headers=alice)
    assert resp.status_code == 422


def test_comment_delete_permissions(client, alice, bob, register, login, create_post):
    register("carol")
    carol = login("carol")
    post = create_post(alice)
    c1 = client.post(f"/posts/{post['id']}/comments", json={"content": "1"}, headers=bob).json()
    c2 = client.post(f"/posts/{post['id']}/comments", json={"content": "2"}, headers=bob).json()

    # 路人不能删
    assert client.delete(f"/comments/{c1['id']}", headers=carol).status_code == 403
    # 评论作者可以删
    assert client.delete(f"/comments/{c1['id']}", headers=bob).status_code == 204
    # 文章作者也可以删
    assert client.delete(f"/comments/{c2['id']}", headers=alice).status_code == 204
    assert client.get(f"/posts/{post['id']}/comments").json() == []


def test_delete_post_cascades_comments(client, alice, bob, create_post):
    post = create_post(alice)
    comment = client.post(
        f"/posts/{post['id']}/comments", json={"content": "hi"}, headers=bob
    ).json()
    assert client.delete(f"/posts/{post['id']}", headers=alice).status_code == 204
    assert client.delete(f"/comments/{comment['id']}", headers=bob).status_code == 404
