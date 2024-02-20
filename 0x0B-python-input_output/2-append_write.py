#!/usr/bin/python3
"""
    Here we have the module descriptions
    Functions:
        - write_file(filename="", text="")
"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
