#!/usr/bin/python3
"""
    Here is the module for the exercise 3-say_my_name
    functions:
        say_my_name(first_name, last_name)
"""


def say_my_name(first_name, last_name=""):
    """
        This function prints my name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
