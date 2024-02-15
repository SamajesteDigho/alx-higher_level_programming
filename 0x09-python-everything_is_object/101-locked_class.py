#!/usr/bin/python3
"""
    Here is the module for exercise 101-locked_class
"""


class LockedClass:
    """The Locked class"""

    def __setattr__(self, __name, __value):
        if __name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(__name))
