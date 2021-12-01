import logging
import datetime


default_format = "%(asctime)22s %(levelname)-8s %(name)s | %(message)s"


class ISO8601UTCTimeFormatter(logging.Formatter):
    converter = datetime.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        current_time = self.converter(record.created).astimezone(datetime.timezone.utc)
        if not datefmt:
            datefmt = "%Y%m%dT%H%M%S.%fZ"
        return current_time.strftime(datefmt)


class DefaultFormatter(ISO8601UTCTimeFormatter):
    pass


class Log:
    def __init__(self, logger=None):
        if isinstance(logger, logging.Logger):
            self.log = logger.getChild(self.__class__.__name__)
        else:
            self.log = logging.getLogger(self.__class__.__name__)


logging.basicConfig(format=default_format)
