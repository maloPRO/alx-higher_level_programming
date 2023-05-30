#!/usr/bin/python3

""" Defines a square """


class Square:
    """
    Creates a square.

    Methods:
        area: finds area of square
        my_print: prints square
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

    def my_print(self):
        """ Prints square using # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#".format(), end="")
                print()
