#!/usr/bin/env python3
"""
Class that inherits from Auth to create a new authentication mechanism
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Class that inherits from Auth to create new authentication mechanism
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Function that creates a Session ID for a user_id"""
        if not user_id or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Function that returns a User ID based on a Session ID"""
        if not session_id or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> str:
        """Retrieves a User instance based on a cookie value.
        """
        cookie_id = self.session_cookie(request)
        if cookie_id is None:
            return None

        user_id = self.user_id_for_session_id(cookie_id)
        if user_id is None:
            return None
        return User.get(user_id)
