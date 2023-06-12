#!/usr/bin/python3

""" Mylist Class """


class MyList(list):
    """
    Class list

    Attributes:
        list: inherited
    """

    def __init__(self, *args):
        """
        Initializes list

        Attributes:
            args: arguments

        Methods:
            print_sorted():  prints sorted list
        """
        super().__init__(*args)

    def print_sorted(self):
        """ Method that prints sorted list """
        print(sorted(self))
