from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    host: str
    port: int
    db: int
    password: str

    model_config = SettingsConfigDict(env_file=".env", env_prefix="REDIS_")

    def get_connection_string(self) -> str:
        if self.password:
            return f"redis://:{self.password}@{self.host}:{self.port}/{self.db}"
        return f"redis://{self.host}:{self.port}/{self.db}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte


redis_settings = RedisSettings()
