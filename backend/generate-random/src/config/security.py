import os
import secrets
from typing import List

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())


class CorsSettings(BaseSettings):
    origins: List[str] = [
        "http://127.0.0.2:9080",  # Frontend
    ]
    add_middleware: List[str] = []


class SecuritySettings(CorsSettings):
    SECRET_KEY: str = str(os.getenv("SECRET_KEY", "default_secret_key"))
    ALGORITHM: str = str(os.getenv("ALGORITHM", "HS256"))
    ACCESS_TOKEN_LIFETIME_IN_MINUTES: int = int(os.getenv("ACCESS_TOKEN_LIFETIME"))
    SESSION_SECRET: str = secrets.token_urlsafe()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte
