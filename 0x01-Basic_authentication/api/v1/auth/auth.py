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
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ Gets the value of the Authorization header from the request
        """
        if request and 'Authorization' in request.headers:
            return request.headers['Authorization']
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user based on the request
        """
        return None
