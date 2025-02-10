from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


# ------------------------------------------------------------------------ #


class DatabaseSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte
