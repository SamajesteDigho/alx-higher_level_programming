#!/usr/bin/python3
"""
    Here we pose the module descriptions
"""


def read_file(filename=""):
    """The function definition documentation"""
    with open(file=filename, encoding="utf-8") as f:
        print(f.read())
