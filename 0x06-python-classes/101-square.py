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
    def __init__(self, size=0, position=(0, 0)):
        """ Constructor for the Square Object
        Note:
            This function is to initilize the object
        Args:
            size: Size of the square
            position: Position coordonate of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size property"""
        if not isinstance(value, int):
            raise TypeError("size must an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for the position propery"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position property"""
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("(x1, x2), x1 and x2 must be >= 0")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square given its size"""
        return self.__size ** 2

    def my_print(self):
        """Displaying the square with # symbols"""
        string = ""
        if self.size == 0:
            string += ""
        else:
            for y in range(self.size + self.position[1]):
                if y < self.position[1]:
                    string += ""
                else:
                    for x in range(self.size + self.position[0]):
                        if x < self.position[0]:
                            string += " "
                        else:
                            string += "#"
                string += '\n'
        print("{}".format(string[:-1]))

    def __str__(self):
        """Overriding the str method to display the square"""
        string = ""
        if self.size == 0:
            string += ""
        else:
            for y in range(self.size + self.position[1]):
                if y < self.position[1]:
                    string += ""
                else:
                    for x in range(self.size + self.position[0]):
                        if x < self.position[0]:
                            string += " "
                        else:
                            string += "#"
                string += '\n'
        return string[:-1]
