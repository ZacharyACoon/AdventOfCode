import logging
import datetime
import sys


class ISO8601UTCTimeFormatter(logging.Formatter):
    converter = datetime.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        current_time = self.converter(record.created).astimezone(datetime.timezone.utc)
        if not datefmt:
            datefmt = "%Y%m%dT%H%M%S.%fZ"
        return current_time.strftime(datefmt)


class ExceptionTracebackSquasherFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def formatException(self, ei):
        return ''


class StdOutErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno <= logging.INFO


class DefaultFormatter(ISO8601UTCTimeFormatter):
    pass


log_format = "%(asctime)22s %(levelname)-8s %(name)s | %(message)s"
formatter = DefaultFormatter(fmt=log_format)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

console_stderr_handler = logging.StreamHandler(sys.stderr)
console_stderr_handler.setFormatter(formatter)
root_logger.addHandler(console_stderr_handler)


log = root_logger


def configure_logging(config):
    key = "log_level"
    if key in config:
        value = config[key].upper()
        if hasattr(logging, value):
            root_logger.setLevel(getattr(logging, value))
        else:
            root_logger.error(f"Config key '{key}' value invalid. {value}")
