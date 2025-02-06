from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgreSQLSettings(BaseSettings):
    """
    Encapsulates the configuration settings for connecting to a PostgreSQL database.

    This class is designed to load database connection parameters from environment
    variables or a configuration file. It uses Pydantic's BaseSettings and supports
    loading configurations dynamically at runtime. The `model_config` attribute specifies
    configuration options such as the path to the environment file and environment variable
    prefix.

    :ivar db_name: Name of the PostgreSQL database.
    :type db_name: str
    :ivar db_user: Username to connect to the database.
    :type db_user: str
    :ivar db_password: Password associated with the database user.
    :type db_password: str
    :ivar db_host: Host address of the PostgreSQL server.
    :type db_host: str
    :ivar db_port: Port number for the PostgreSQL database.
    :type db_port: int
    """

    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    model_config = SettingsConfigDict(env_file=".env", env_prefix="POSTGRES_")

    def get_connection_string(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignoriere zusätzliche Eingabewerte


postgres_settings = PostgreSQLSettings()
