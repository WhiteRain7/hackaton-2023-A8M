from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from pathlib import Path


class Settings(BaseSettings):
    app_title: str = "API pitch-deck"
    app_description: str = "API pitch-deck"
    app_version: str = "0.0.1"
    media_path: Path = Path().absolute() / "app" / "media"
    templates_path: Path = Path().absolute() / "app" / "templates"
    origins: list[AnyHttpUrl] | list[str] = ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
