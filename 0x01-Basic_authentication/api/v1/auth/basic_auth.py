#!/usr/bin/env python3
""" Authentication Module """
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """
    Basic Auth class
    """
    pass
