#!/usr/bin/env python3
""" Logging module """
from typing import List
import re


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
