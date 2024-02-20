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
    with open(filename, "r") as f:
        print("{}".format(f.read()))
