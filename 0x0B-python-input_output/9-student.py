#!/usr/bin/python3
"""
    Here the description of the module
"""


class Student:
    """Here the description of the function"""

    def __init__(self, first_name, last_name, age):
        """Initialisation of the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Getting the dict representation"""
        return self.__dict__
