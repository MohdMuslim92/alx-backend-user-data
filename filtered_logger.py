#!/usr/bin/env python3
"""
filtered_logger module
"""

import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """
    Replaces specified fields in a log message with redaction.

    Args:
        fields: a list of strings representing fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character separates all
        fields in the log line

    Returns:
        The log message with specified fields obfuscated.
    """
    pattern = re.compile(f'({"|".join(fields)}=)[^{separator}]*')
    return pattern.sub(fr'\1{redaction}', message)
