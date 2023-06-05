#!/usr/bin/python3

""" Defines a rectangle """


class Rectangle:
    """Creates a Rectangle  """

    def __init__(self, width=0, height=0):
        """
        Initializes instance of a rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.__width = width
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """ Gets width """
        return self.__width

    @property
    def height(self):
        """ Gets height """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets new width size

        Args:
            value(int): The new width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets new height size

        Args:
            value(int): The new width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
