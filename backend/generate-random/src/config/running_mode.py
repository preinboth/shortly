import os

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())


class RunningModeSettings(BaseSettings):
    API_DEBUG: bool = os.getenv("API_DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte
