#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square Object module.
This module defines the Square Object class and all the functions
with the given properties and methods
Example:
    Square(size, position)
"""


class Square:
    """ Here is the class which defines the Square Object."""
    def __init__(self, size=0):
        """ Constructor for the Square Object
        Note:
            This function is to initilize the object
        Args:
            size: Size of the square
        """
        try:
            if type(size) is not type(0):
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size: int = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
