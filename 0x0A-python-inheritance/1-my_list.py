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
        """
        super().__init__(*args)

    def print_sorted(self):
        """
        sorts list
        """
        print(self.sort())


