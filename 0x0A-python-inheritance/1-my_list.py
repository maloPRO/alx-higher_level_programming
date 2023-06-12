#!/usr/bin/python3

""" Mylist Class """


class MyList(list):
    """
    Class list

    Attributes:
        list: inherited

    Methods:
        print_sorted(): prints sorted list
    """

    def __init__(self):
        """ Initializes MyList Class  """

    def print_sorted(self):
        """ Method that prints sorted list """
        print(sorted(self))
