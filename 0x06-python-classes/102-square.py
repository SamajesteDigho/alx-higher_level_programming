#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square Object module.
This module defines the Square Object class and all the functions
with the given properties and methods
Example:
    Square(size, position)
"""


class Square:
    """
        Here is the class which defines the Square Object.
    """
    def __init__(self, size=0):
        """ Constructor for the Square Object
        Note:
            This function is to initilize the object
        Args:
            size: Size of the square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square given its size"""
        return self.size ** 2

    def __eq__(self, other):
        """== operator taken in charge by the object"""
        return self.area() == other.area()

    def __neq__(self, other):
        """!= operator taken in charge by the object"""
        return self.area() != other.area()

    def __gt__(self, other):
        """> operator taken in charge by the object"""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= operator taken in charge by the object"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """< operator taken in charge by the object"""
        return self.area() < other.area()

    def __le__(self, other):
        """<= operator taken in charge by the object"""
        return self.area() <= other.area()
