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
    """Replaces specified fields in a log message with redaction."""
    pattern = re.compile(f'({"|".join(fields)}=)[^{separator}]*')
    return pattern.sub(fr'\1{redaction}', message)
