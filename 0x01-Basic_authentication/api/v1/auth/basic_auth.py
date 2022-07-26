#!/usr/bin/env python3
""" Authentication Module """
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import base64


class BasicAuth(Auth):
    """
    Basic Auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ The function extracts the endocded string from the header"""
        if not authorization_header:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ The function decodes the Authorization in header """
        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            string = base64_authorization_header.encode('utf-8')
            dcode = base64.decodebytes(string)
        except Exception:
            return None
        return dcode.decode()
