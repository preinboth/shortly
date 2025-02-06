import logging


class NoBadWordsFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.getMessage().__contains__("f")
