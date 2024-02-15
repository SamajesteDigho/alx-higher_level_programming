#!/usr/bin/python3
"""
    Here is the module for the exercise 0-add_integer
    functions:
        add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
        This function permits to add 2 numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(int(a) + int(b))
