#!/usr/bin/python3
"""
    Definition of the file module for the Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Definition de la class Rectangle fils de BaseGeometry"""

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle"""
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
