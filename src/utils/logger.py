import logging
import sys
from functools import lru_cache
import json

def configure_logging():
    logging.root.handlers.clear()

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(lambda record: record.levelno < logging.WARNING)
    stdout_handler.setFormatter(formatter)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(formatter)


    logging.basicConfig(level=logging.DEBUG, handlers=[stdout_handler, stderr_handler])



class LoggerWrapper:
    """Temporary logger impl"""
    def __init__(self, logger: logging.Logger):
        self.__logger = logger

    def info(self, message: str, **context):
        self.__logger.info(message + " " + str(context))

    def debug(self, message: str, **context):
        self.__logger.debug(message + " " + str(context))

    def warning(self, message: str, **context):
        self.__logger.warning(message + " " + str(context))

    def critical(self, message: str, **context):
        self.__logger.critical(message + " " + str(context))

    def error(self, message: str, **context):
        self.__logger.error(message + " " + str(context))


@lru_cache(maxsize=None)
def get_logger(name: str, level=logging.DEBUG) -> LoggerWrapper:
    configure_logging()
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return LoggerWrapper(logger)
