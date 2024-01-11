#!/usr/bin/env python3
"""
filtered_logger module
"""

import re
from typing import List


pattern = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """Replaces specified fields in a log message with redaction."""
    extract, replace = (pattern["extract"], pattern["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
