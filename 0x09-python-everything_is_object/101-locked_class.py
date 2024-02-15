#!/usr/bin/python3
"""
    Here is the module for exercise 101-locked_class
"""


class LockedClass:
    """The Locked class"""

    def __setattr__(self, __name, __value):
        """Specifying the attributes to select"""
        if __name != "first_name":
            err = "'LockedClass' object has no attribute '{}'".format(__name)
            raise AttributeError(err)
        super().__setattr__(__name, __value)
