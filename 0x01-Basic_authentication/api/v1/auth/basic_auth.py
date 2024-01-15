#!/usr/bin/env python3
"""
Basic authentication module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class for API authentication
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ Extracts the Base64 part of the Authorization header for Basic
        Authentication
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        # Check if the header starts with 'Basic ' and has at least one
        # character after the space
        if not authorization_header.startswith('Basic '):
            return None

        # Extract the Base64 part after 'Basic '
        base64_part = authorization_header.split(' ')[1]

        return base64_part
