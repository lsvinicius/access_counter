import logging
from logging.handlers import TimedRotatingFileHandler

from src.settings import get_log_file_path


def _logger() -> logging.Logger:
    lg = logging.getLogger('AccessCounter')
    lg.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(get_log_file_path(), when="m", interval=1)
    lg.addHandler(handler)
    return lg


logger = _logger()
