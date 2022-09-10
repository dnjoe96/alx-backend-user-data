#!/usr/bin/env python3
""" Logging module """
from typing import List
import re
import logging


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

    def __init__(self, strings: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError

