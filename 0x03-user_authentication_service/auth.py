#!/usr/bin/env python3
""" Module for Auth """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ The function hashes a password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes(password.encode('utf-8')), salt)
