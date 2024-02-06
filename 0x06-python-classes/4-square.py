#!/usr/bin/python3
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
        if type(size) is not type(0):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if type(value) is not type(0):
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
                self.__size: int = value
        except TypeError:
            raise TypeError("size must an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square given its size"""
        return self.size ** 2
