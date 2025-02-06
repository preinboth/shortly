from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

from src.config import _DATA_DIR, _LOGS_DIR

load_dotenv(find_dotenv())


class MediaSettings(BaseSettings):
    DATA_DIR: Path = _DATA_DIR
    LOGS_DIR: Path = _LOGS_DIR

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte
