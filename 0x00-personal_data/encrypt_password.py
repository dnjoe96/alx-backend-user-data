#!/usr/bin/env python3
""" Module to manage password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Function to hash password with salt and return
    byte string password """
    passwrd = password.encode()
    hashed = bcrypt.hashpw(passwrd, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Function to validate if password matches a hashed password """
    passwrd = password.encode()
    if bcrypt.checkpw(passwrd, hashed_password):
        return True
    else:
        return False
