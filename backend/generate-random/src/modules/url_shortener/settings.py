from pydantic import BaseConfig


class Settings(BaseConfig):
	SHORT_LENGTH_DEFAULT: int = 7
	SHORT_LENGTH_MIN: int = 7
	SHORT_LENGTH_MAX: int = 7
	QUANTITY_DEFAULT = 1
	QUANTITY_MIN = 1
	QUANTITY_MAX = 500
	class Config:
		env_file = ".env"
		env_file_encoding = "utf-8"


settings = Settings()
