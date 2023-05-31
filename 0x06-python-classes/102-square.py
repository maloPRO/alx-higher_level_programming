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

    @property
    def size(self):
        """ Gets size """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Mutates size of square

        Args:
            value(int): NEw value of square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Gets area of square """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Checks if value is equal

        Args:
            value(int): other value
        """

        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if value is not equal

        Args:
            value(int): other value
        """

        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if value is greater than

        Args:
            value(int): other value
        """

        return self.area() > other.area()

    def __lt__(self, other):
        """
        Checks if value is less than

        Args:
            value(int): other value
        """

        return self.area() < other.area()

    def __ge__(self, other):
        """
        Checks if value is greater than or equal to

        Args:
            value(int): other value
        """

        return self.area() >= other.area()

    def __le__(self, other):
        """
        Checks if value is less than or equal to

        Args:
            value(int): other value
        """

        return self.area() <= other.area()
