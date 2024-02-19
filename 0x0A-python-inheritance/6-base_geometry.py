#!/usr/bin/python3
"""
    Definition of the file module for the Geometrie class
"""


class BaseGeometry:
    """Definition of class BaseGeometry"""

    def area(self):
        """Returns the area of the geometric figure"""
        raise Exception("area() is not implemented")
