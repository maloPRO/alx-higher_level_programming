#!/usr/bin/python3

""" Defines a square """


class Square:
    """
    Creates a square.

    Methods:
        area: finds area of square
    """

    def __init__(self, size=0):
        """
        Initializes an instance of square

        Args:
            size(int): size of the square.
        """
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ GEts area of square """
        return self.__size * self.__size
