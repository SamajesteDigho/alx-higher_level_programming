#!/usr/bin/pyhon3
""" This is the file defining the Rectangle class

    Rectangle inherits from Base class defined in this same module
    and the defines additional fields.
"""
from base import Base


class Rectangle(Base):
    """ This is the Rectangle class which inherits from Base and
        defines some new fields as follows:

        Attributs: width, height, x, y

        Methods: Getters and Setters
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area  of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle"""
        string = ""
        for i in range(self.__height + self.__y):
            if i < self.__y:
                string += "\n"
            else:
                for j in range(self.__width + self.__x):
                    if j < self.__x:
                        string += " "
                    else:
                        string += "#"
                string += "\n"
        print("{}".format(string.rstrip()))

    def __str__(self):
        """Return the str representation of the Rectangle"""
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                         self.__x, self.__y,
                                                         self.__width,
                                                         self.__height)
        return string

    def update(self, *args, **kwargs):
        """Update attributes by args parameter"""
        if args is not None and len(args) > 0:
            for i, value in enumerate(list(args)):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.width = value
                elif i == 2:
                    self.height = value
                elif i == 3:
                    self.x = value
                elif i == 4:
                    self.y = value
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """Returning the dictionary representation of Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
