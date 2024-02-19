#!/usr/bin/python3
"""
    Module for the file 101-add_attribute
"""


def add_attribute(obj, name, value):
    """Definition of this ununderstanding function"""
    if obj.__setattr__(name, value):
        raise TypeError("can't add new attribute")
