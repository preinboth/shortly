from pydantic_settings import BaseSettings, SettingsConfigDict


class SQLiteSettings(BaseSettings):
    db_name: str = "database.sqlite"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="SQLITE_")

    def get_connection_string(self) -> str:
        return f"sqlite:///{self.db_name}"

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte


sqlite_settings = SQLiteSettings()
