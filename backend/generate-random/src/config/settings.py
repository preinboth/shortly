from dotenv import find_dotenv, load_dotenv

from config.database.databases import DatabaseSettings
from config.media import MediaSettings
from config.openapi import OpenApiSettings
from config.running_mode import RunningModeSettings
from config.security import SecuritySettings
from config.server import ServerSettings

load_dotenv(find_dotenv())


class Settings(
    ServerSettings,
    SecuritySettings,
    OpenApiSettings,
    DatabaseSettings,
    MediaSettings,
    RunningModeSettings,
):
    API_BASE_PATH: str = "/"

    SWAGGER_UI_DOC_EXPANSION: str = "list"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignore zusätzliche Eingabewerte


settings = Settings()
