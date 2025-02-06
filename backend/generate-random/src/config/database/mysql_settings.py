from pydantic_settings import BaseSettings, SettingsConfigDict


class MySQLSettings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    model_config = SettingsConfigDict(env_file=".env", env_prefix="MYSQL_")

    def get_connection_string(self) -> str:
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte


mysql_settings = MySQLSettings()
