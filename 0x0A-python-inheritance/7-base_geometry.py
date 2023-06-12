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
            return False
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
            return False
        return True
