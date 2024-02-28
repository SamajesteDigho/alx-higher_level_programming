#!/usr/bin/python3
""" This is the file in which is defined the Square class

    It inherits from the Rectangle class found in the same module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the Square class object which inherits
        from the Rectangle class.
        Defines new fields and shallow some from the rectangle class

        Attributs: size // width, height
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation of the Square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the str representation of the rectangle"""
        string = "[Square] ({}) {}/{} - {}".format(self.id,
                                                   self.x, self.y,
                                                   self.width)
        return string

    def update(self, *args, **kwargs):
        """Update attributes by args parameter"""
        if args is not None and len(args) > 0:
            for i, value in enumerate(list(args)):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.width = value
                    self.height = value
                elif i == 2:
                    self.x = value
                elif i == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """Returning the dictionary representation of Rectangle"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
