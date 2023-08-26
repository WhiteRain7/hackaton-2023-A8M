from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl
from pathlib import Path
from hugchat import hugchat

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    app_title: str = "API pitch-deck"
    app_description: str = "API pitch-deck"
    app_version: str = "0.0.1"
    media_path: Path = Path().absolute() / "app" / "media"
    templates_path: Path = Path().absolute() / "app" / "templates"
    origins: list[AnyHttpUrl] | list[str] = ["*"]
    hugchat_email: str
    hugchat_pwd: str
    chatbot: hugchat.ChatBot | None = None
    cookie_path: Path = Path().absolute() / "cookies_snapshot"


settings = Settings()
