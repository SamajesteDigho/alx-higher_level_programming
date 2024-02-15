#!/usr/bin/python3
"""
    Here is the module for the exercise 4-print_square
    functions:
        print_square(size)
"""


def print_square(size):
    """
        This function prints a square given the size
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print("")
