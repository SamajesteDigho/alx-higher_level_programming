#!/usr/bin/python3
"""
    Here we have the module descriptions
    Functions:
        - write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
        The function definition documentation
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
