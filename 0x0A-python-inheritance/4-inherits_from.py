#!/usr/bin/python3
"""
    Definition of the file module for 4-inherits_from
"""


def inherits_from(obj, a_class):
    """Check innheritance direct or indirect"""
    return isinstance(obj, a_class) and type(obj) is not a_class
