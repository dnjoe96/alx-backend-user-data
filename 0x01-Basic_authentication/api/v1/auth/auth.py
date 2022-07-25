#!/usr/bin/env python3
""" Authentication Module """
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ function to determine path that require auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Generates auth header"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ Function to return current user"""
        return request
