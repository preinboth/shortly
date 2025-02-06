import logging

from . import filter
from .formatter import formatter
from .utils import get_logFilePath

logfile = get_logFilePath()

# * -------- File Handler --------- *
# file_handler = logging.FileHandler(filename='/src/data/log.log')
file_handler = logging.FileHandler(filename=logfile)
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
file_handler.addFilter(filter.NoBadWordsFilter())

# * -------- Stream Handler --------- *
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
stream_handler.addFilter(filter.NoBadWordsFilter())
