from pydantic_settings import BaseSettings

class _BaseSettingsWithEnv(BaseSettings):
    # 配置读取方式
    # env文件的位置;文件里还有其他配置组的变量(如 WEB_*),这里忽略多余字段
    model_config = {"env_file": ".env.example", "extra": "ignore"}

class CommonSetting(BaseSettings):
    environment: str = "development"

class WebSetting(BaseSettings):
    app_name: str = "Web Service API"

    model_config = {
        "env_file": ".env",
        "env_prefix": "WEB_"
    }
# 数据库配置
class _DBSettings(_BaseSettingsWithEnv):
    host: str = ""
    port: str = ""
    name: str = ""
    user: str = ""
    password: str = ""

    model_config = {"env_prefix": "DB_"}

common_settings = CommonSetting()
web_settings = WebSetting()
db_settings = _DBSettings()

