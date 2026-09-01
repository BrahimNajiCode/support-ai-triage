from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Support AI Triage"
    app_version: str = "0.1.0"
    environment: str = "development"

    api_v1_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

# Least Recently Used, default is 128.
@lru_cache
def get_settings() -> Settings:
    return Settings()