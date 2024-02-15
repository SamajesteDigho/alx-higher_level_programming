#!/usr/bin/python3
"""
    Here is the module for exercise 101-locked_class
"""


from typing import Any


class LockedClass:
    """The Locked class"""

    def __getattribute__(self, __name: str):
        """Specifying the attributes to getter"""
        if __name != "first_name":
            err = "'LockedClass' object has no attribute '{}'".format(__name)
            raise AttributeError(err)
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        """Specifying the attributes to setter"""
        if __name != "first_name":
            err = "'LockedClass' object has no attribute '{}'".format(__name)
            raise AttributeError(err)
        super().__setattr__(__name, __value)
