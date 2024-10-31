#!/usr/bin/python3
"""
Module for UTF-8 validation.
This module provides a method to determine if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes of data.

    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise.
    """
    expected_continuation = 0

    for byte in data:
        # Keep only the 8 least significant bits
        current_byte = byte & 0xFF

        if expected_continuation > 0:
            # Check if byte is a valid continuation byte (starts with 10)
            if (current_byte & 0b11000000) != 0b10000000:
                return False
            expected_continuation -= 1
            continue

        # Determine number of continuation bytes needed
        if (current_byte & 0b10000000) == 0:
            # 1-byte character (0xxxxxxx)
            expected_continuation = 0
        elif (current_byte & 0b11100000) == 0b11000000:
            # 2-byte character (110xxxxx)
            expected_continuation = 1
        elif (current_byte & 0b11110000) == 0b11100000:
            # 3-byte character (1110xxxx)
            expected_continuation = 2
        elif (current_byte & 0b11111000) == 0b11110000:
            # 4-byte character (11110xxx)
            expected_continuation = 3
        else:
            # Invalid starting byte
            return False

    # Check if all characters were properly completed
    return expected_continuation == 0
