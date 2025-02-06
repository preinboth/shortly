import os

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())

summary = "Collection of Shortly - Random-Generator-Service"
description = """
Description of Shortly - Random-Generator-Service
"""


class ServerSettings(BaseSettings):
    HOST: str = os.getenv("HOST")
    PORT: int = os.getenv("PORT")
    BASE_URL: str = f"{os.getenv("PROTOKOLL")}://{HOST}:{PORT}"

    API_TITLE: str = os.getenv("PROJECT_NAME")
    API_SUMMARY: str = summary
    API_DESCRIPTION: str = description
    API_TERMS_OF_SERVICE: str = "http://example.com/terms/"
    API_VERSION: str = "0.0.1"

    API_CONTACT_NAME: str = "Contact name"
    API_CONTACT_URL: str = "https://www.example.com"
    API_CONTACT_EMAIL: str = "contact@example.com"

    API_LICENCE_NAME: str = "License"
    API_LICENCE_URL: str = "https://www.license.example.com"

    API_PREFIX: str = "api"
    API_BASE_PATH: str = "/"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte


server_settings = ServerSettings()
