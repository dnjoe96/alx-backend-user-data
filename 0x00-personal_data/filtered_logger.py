#!/usr/bin/env python3
""" Logging module """
from typing import List
import re
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ returns the log message obfuscated """
    temp = message
    # print(temp)
    for field in fields:
        # print(field)
        temp = re.sub(field + "=.*?" + separator,
                      field + "=" + redaction + separator, temp)
    return temp


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ A function that formats log record """
        formatted_record = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            formatted_record, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Creates and returns a logger."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger
