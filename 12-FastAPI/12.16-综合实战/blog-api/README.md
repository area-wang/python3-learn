# Blog API

FastAPI 综合实战项目：用户注册登录（OAuth2 密码流 + JWT）、文章 CRUD（分页 / 搜索 / 标签过滤）、评论、统一错误格式、请求 ID 中间件。

详细讲解见上级目录的 [用法.md](../用法.md)，扩展任务见 [练习题.md](../练习题.md)。

## 技术栈

- FastAPI + Uvicorn
- SQLAlchemy 2.x（同步 Session）+ SQLite（可换 PostgreSQL）
- Pydantic v2 / pydantic-settings
- PyJWT + pwdlib（Argon2）
- pytest + TestClient

## 快速开始

### 方式一：uv（推荐）

```bash
cd blog-api
cp .env.example .env          # 可选，不复制则使用默认配置
uv sync                       # 创建 .venv 并安装依赖（含 dev 组）
uv run fastapi dev            # 入口已在 pyproject.toml 的 [tool.fastapi] 中配置为 app.main:app
                              # 等价于 uv run fastapi dev app/main.py
```

> ⚠️ 入口文件是 `app/main.py`，不是 `main.py`。`uv run fastapi dev main.py` 会报 `Path does not exist main.py`。

### 方式二：pip

```bash
cd blog-api
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install "fastapi[standard]" "sqlalchemy>=2" pydantic-settings pyjwt "pwdlib[argon2]" pytest httpx
fastapi dev app/main.py
```

启动后访问：

- 交互式文档：http://127.0.0.1:8000/docs （右上角 Authorize 可直接登录）
- ReDoc：http://127.0.0.1:8000/redoc
- 健康检查：http://127.0.0.1:8000/health

## 运行测试

```bash
uv run pytest          # 或激活虚拟环境后：pytest
```

测试使用内存 SQLite，不会生成数据库文件。

## 接口一览

| 方法 | 路径 | 说明 | 需登录 |
|---|---|---|---|
| POST | `/auth/register` | 注册 | |
| POST | `/auth/token` | 登录，表单提交，返回 JWT | |
| GET | `/users/me` | 当前用户 | ✅ |
| PATCH | `/users/me` | 修改邮箱 / 简介 / 密码 | ✅ |
| GET | `/users/{user_id}` | 公开资料 | |
| GET | `/posts` | 文章列表：`page` `size` `q` `tag` `author_id` | |
| POST | `/posts` | 发文章 | ✅ |
| GET | `/posts/{post_id}` | 文章详情（含评论） | |
| PATCH | `/posts/{post_id}` | 修改（仅作者） | ✅ |
| DELETE | `/posts/{post_id}` | 删除（仅作者，级联删除评论） | ✅ |
| GET | `/posts/{post_id}/comments` | 评论列表 | |
| POST | `/posts/{post_id}/comments` | 发表评论 | ✅ |
| DELETE | `/comments/{comment_id}` | 删除（评论作者或文章作者） | ✅ |
| GET | `/health` | 健康检查 | |

## 配置

所有配置项见 `app/core/config.py`，通过 `BLOG_` 前缀的环境变量或 `.env` 文件覆盖，例如：

```bash
BLOG_DATABASE_URL=sqlite:///./dev.db BLOG_DEBUG=true uv run fastapi dev app/main.py
```
