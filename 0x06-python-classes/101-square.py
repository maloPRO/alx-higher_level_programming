#!/usr/bin/python3

""" Defines a square """


class Square:
    """
    Creates a square.

    Methods:
        area: finds area of square
        my_print: prints square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance of square

        Args:
            size(int): size of the square.
        """
        self.__size = size
        self.__position = position

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """ Gets size """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Mutates size of square

        Args:
            value(int): New value of square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Gets position """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets new position

        Args:
            value: new position to be set
        """
        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ Gets area of square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints square using # """
        if self.__size == 0:
            print()
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
