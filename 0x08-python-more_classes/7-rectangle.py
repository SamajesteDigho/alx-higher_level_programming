#!/usr/bin/python3
"""
    Module for the representation of the class Rectangle
"""


class Rectangle:
    """
    Here is the class Rectangle docstring
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Iniialization of the class"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter of the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.height + self.width)

    def __str__(self):
        """Returns the string representation of Rectangle"""
        string = ""
        for _ in range(self.height):
            for _ in range(self.width):
                string += "{}".format(self.print_symbol)
            string += '\n'
        return string.strip()

    def __repr__(self):
        """Returns the official representation of Rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deleting an instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
