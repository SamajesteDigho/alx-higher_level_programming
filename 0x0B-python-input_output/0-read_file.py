#!/usr/bin/python3
"""
    Here we pose the module descriptions
"""


def read_file(filename=""):
    """The function definition documentation"""
    with open(filename, encoding="utf-8") as f:
        print("{}".format(f.read()))
