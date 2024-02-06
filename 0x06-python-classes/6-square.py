#!/usr/bin/python3
class Square:
    """Here is the class which defines the Square Object."""

    def __init__(self, size=0, position=(0, 0)):
        """Here is the constructor of an instance of the Square Object
        Args:
            size: Size of the square instance
        """
        self.size = size
        self.position = position

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
                self.__size = value
        except TypeError:
            raise TypeError("size must an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if type(value) is not type((0, 0)):
                raise TypeError
            elif value[0] < 0 or value[1] < 0:
                raise ValueError
            else:
                self.__position = value
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        except ValueError:
            raise ValueError("value must be >= 0")

    def area(self):
        """Returns the area of the square given its size"""
        return self.size ** 2

    def my_print(self):
        """Displaying the square with # symbols"""
        if self.size == 0:
            print("")
        else:
            for y in range(self.size + self.position[1]):
                if y < self.position[1]:
                    print("", end='')
                else:
                    for x in range(self.size + self.position[0]):
                        if x < self.position[0]:
                            print(" ", end='')
                        else:
                            print("#", end='')
                print("")
