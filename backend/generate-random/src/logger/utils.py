from pathlib import Path

from src.config.settings import settings


class MyPathLike(Path):
    def __fspath__(self):
        return str(self.as_posix())


def get_logFilePath() -> str:
    # t = MyPathLike(api_settings.DATA_DIR.resolve()).joinpath("logs").joinpath('log.log')
    t = MyPathLike(settings.LOGS_DIR.resolve()).joinpath("log.log")
    return t
