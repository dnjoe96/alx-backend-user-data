#!/usr/bin/env python3
""" Module for Auth """
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ The function hashes a password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes(password.encode('utf-8')), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ constructor method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ This method is used to register a user"""
        user = DB.find_user_by(email=email)
        if user:
            raise ValueError('<user\'s email> already exists>')
        password = _hash_password(password).decode('utf-8')
        # user = User(email=email, hashed_password=password)
        return self._db.add_user(email=email, hashed_password=password)
