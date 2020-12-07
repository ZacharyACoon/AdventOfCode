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


def get_logger(name=None):
    logger = logging.getLogger(name=name)
    return logger


logging.basicConfig(format=default_format)
