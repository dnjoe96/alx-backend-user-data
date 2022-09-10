#!/usr/bin/env python3
""" Logging module """
from typing import List
import re
import logging
import mysql.connector
import os

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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Connects to a MySQL database and returns a connector to the database"""
    hostname = os.getenv("PERSONAL_DATA_DB_HOST")
    dbname = os.getenv("PERSONAL_DATA_DB_NAME")
    user_name = os.getenv("PERSONAL_DATA_DB_USERNAME")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    connector_variables = {"host": hostname,
                           "database": dbname,
                           "username": user_name,
                           "password": password}
    try:
        connection = mysql.connector.connect(**connector_variables)
        return connection
    except mysql.connector.Error as e:
        print("Error: ", e)


def main() -> None:
    """ Main function """
    columns = ["name", "email", "phone", "ssn", "password", "ip", "last_login",
               "user_agent"]
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        series = map(lambda x: "{}={}".format(x[0], x[1]), zip(columns, row))
        log_message = "{}".format("; ".join(list(series)))
        log_record = logging.LogRecord(
            "user_data", logging.INFO, None, None, log_message, None, None)
        logger.handle(log_record)
    cursor.close()
    db.close()
