#!/usr/bin/env python3
""" Authentication module.
This module provides functions for user authentication, including password
hashing.

"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes the input password using bcrypt.hashpw.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
