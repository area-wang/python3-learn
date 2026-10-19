from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用配置。

    读取优先级：环境变量（前缀 BLOG_） > .env 文件 > 这里的默认值。
    例如 BLOG_DATABASE_URL=postgresql+psycopg://... 会覆盖 database_url。
    """

    model_config = SettingsConfigDict(env_prefix="BLOG_", env_file=".env", extra="ignore")

    app_name: str = "Blog API"
    debug: bool = False
    database_url: str = "sqlite:///./blog.db"

    secret_key: str = "dev-only-secret-key-change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    cors_origins: list[str] = ["http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    """全局只创建一次 Settings；测试中可用 get_settings.cache_clear() 重新加载。"""
    return Settings()
