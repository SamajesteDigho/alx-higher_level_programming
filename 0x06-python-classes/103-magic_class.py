#!/usr/bin/python3
import math
"""
    Here the awaited description of the module.
    More is still to come
"""


class MagicClass:
    """MagicClass object characteristics description"""
    
    def __init__(self, radius=0):
        """Constructor for the Magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculating the area of the circle"""
        return math.pow(self.__radius, 2) * math.pi

    def circumference(self):
        """Calculating the circumference of the circle"""
        return 2 * math.pi * self.__radius
