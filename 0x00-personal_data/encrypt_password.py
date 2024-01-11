#!/usr/bin/env python3
"""
This module provides a function for hashing passwords using the bcrypt hashing
algorithm with salt. 
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
