#!/usr/bin/python3
class Square:
    """Here is the class which defines the Square Object."""

    def __init__(self, size=0):
        """Here is the constructor of an instance of the Square Object
        Args:
            size: Size of the square instance
        """
        self.size = size

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

    def my_print(self):
        """Displaying the square with # symbols"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                for _ in range(self.size):
                    print("#", end='')
                print("")
