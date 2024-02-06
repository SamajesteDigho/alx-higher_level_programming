#!/usr/bin/python3
class Square:
    """Here is the class which defines the Square Object."""

    def __init__(self, size=0):
        """Here is the constructor of an instance of the Square Object
        Args:
            size: Size of the square instance
        """
        try:
            if type(size) is not type(0):
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size: int = size
        except TypeError:
            TypeError("size must an integer")
        except ValueError:
            ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square given its size"""
        return self.__size ** 2
