#!/usr/bin/env python3
"""
SessionAuth module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID for a user_id """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a Session ID using uuid module and uuid4()
        session_id = str(uuid.uuid4())

        # Use this Session ID as the key of the dictionary
        # user_id_by_session_id, the value for this key must be user_id
        self.user_id_by_session_id[session_id] = user_id

        # Return the Session ID
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieve a User ID based on a Session ID """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
