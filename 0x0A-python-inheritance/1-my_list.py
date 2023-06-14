#!/usr/bin/python3

"""
This module contains a  custom list class that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from list

    Attributes:
        list: inherited

    Methods:
        print_sorted(): prints sorted list
    """

    def __init__(self):
        """ Initializes MyList Class  """
        super().__init__()

    def print_sorted(self):
        """ Method that prints sorted list """
        print(sorted(self))
