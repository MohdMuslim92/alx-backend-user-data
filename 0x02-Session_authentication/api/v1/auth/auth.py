#!/usr/bin/env python3
""" Authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for a given path
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        elif path in excluded_paths:
            return False

        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Gets the value of the Authorization header from the request
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

        if request and 'Authorization' in request.headers:
            return request.headers['Authorization']
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user based on the request
        """
        return None
