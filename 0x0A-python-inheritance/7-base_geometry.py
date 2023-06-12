#!/usr/bin/python3

""" Geometry class """


class BaseGeometry:
    """ Does geometry """

    def area(self):
        """ raises error """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name (str): name
            value (int): value

        Returns:
            bool: True or false

        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
