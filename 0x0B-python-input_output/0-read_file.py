#!/usr/bin/python3
"""
    Here we have the module descriptions
    Functions:
        - read_file(filename)
"""


def read_file(filename=""):
    """
        The function definition documentation
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        if len(content.strip()) > 0:
            print("{}".format(content.strip()))
