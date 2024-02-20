#!/usr/bin/python3
"""
    Definition of the file module for the Geometrie class
"""


class BaseGeometry:
    """Definition of class BaseGeometry"""

    def __init__(self):
        """Initialization of BaseGeometry"""

    def area(self):
        """Returns the area of the geometric figure"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate and integer value"""
        if not issubclass(type(value), int) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
