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

    def to_json(self, attrs=None):
        """Getting the dict representation"""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            res = {}
            for x in self.__dict__.keys():
                if x in attrs:
                    res[x] = self.__getattribute__(x)
            return res
        elif attrs is None:
            return self.__dict__

    def reload_from_json(self, json):
        """Reloadng json"""
        for x in json.keys():
            self.__setattr__(x, json[x])
