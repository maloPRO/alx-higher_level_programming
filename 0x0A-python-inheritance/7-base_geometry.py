#!/usr/bin/python3

""" Geometry class """


class BaseGeometry:
    """
    Does geometry

    Methods:
        area():raises exception
        integer_validator(): validates a value
    """

    def area(self):
        """ raises exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name (str): name
            value (int): value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
