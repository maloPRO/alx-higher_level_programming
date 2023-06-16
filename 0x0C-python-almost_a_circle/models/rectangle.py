#!/usr/bin/python3

""" This module contains a class that defines a rectangle """

from  models.base import Base

class Rectangle(Base):
    """ Defines a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes rect """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """ Gets width """
        return self.__width

    @property
    def height(self):
        """ Gets height """
        return self.__height

    @property
    def x(self):
        """ Gets X """
        return self.__x

    @property
    def y(self):
        """ Gets Y """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Sets new width

        Args:
            value: new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets new heigh

        Args:
            value: new height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets new x

        Args:
            value: new x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets new y

        Args:
            value: new y value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
