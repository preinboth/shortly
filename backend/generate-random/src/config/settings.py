from dotenv import find_dotenv, load_dotenv

from src.config.database.databases import DatabaseSettings
from src.config.media import MediaSettings
from src.config.openapi import OpenApiSettings
from src.config.qrcode_settings import QrCodeSettings
from src.config.running_mode import RunningModeSettings
from src.config.security import SecuritySettings
from src.config.server import ServerSettings
from src.config.shortener_settings import UrlShortenerSettings
from src.config.uuid_settings import UuidSettings

load_dotenv(find_dotenv())


class Settings(
    ServerSettings,
    SecuritySettings,
    OpenApiSettings,
    DatabaseSettings,
    MediaSettings,
    QrCodeSettings,
    UrlShortenerSettings,
    UuidSettings,
    RunningModeSettings,
):
    API_BASE_PATH: str = "/"

    SWAGGER_UI_DOC_EXPANSION: str = "list"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte


settings = Settings()
