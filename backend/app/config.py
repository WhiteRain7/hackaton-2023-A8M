from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "API pitch-deck"
    app_description: str = "API pitch-deck"
    app_version: str = "0.0.1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
