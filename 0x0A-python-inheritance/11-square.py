#!/usr/bin/python3
"""
    Definition of the file module for the Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Definition of class Square son of Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """String representation of the rectangle"""
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
