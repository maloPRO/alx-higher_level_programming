#!/usr/bin/python3

""" Defines a rectangle """


class Rectangle:
    """Creates a Rectangle  """

    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Finds the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Finds perimeter of rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ returns string rep """

        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            if i < self.__height - 1:
                rectangle_str += str(self.print_symbol) * self.__width + "\n"
            else:
                rectangle_str += str(self.print_symbol) * self.__width
        return rectangle_str

    def __repr__(self):
        """ Returns str rep """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ detects instance of deletion """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
