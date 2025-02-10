from typing import ClassVar

from pydantic_settings import BaseSettings


class UuidSettings(BaseSettings):
    UUID_QUANTITY_DEFAULT: ClassVar[int] = 1
    UUID_QUANTITY_MIN: ClassVar[int] = 1
    UUID_QUANTITY_MAX: ClassVar[int] = 500

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
