#!/usr/bin/python3

""" checks if object is instance of a class """


def inherits_from(obj, a_class):
    """
    Chcks if object is instance af a_class

    Args:
        obj (object): object to be checked
        a_class (object): class to be checked

    Returns:
        bool: True or false
    """

    return issubclass(obj, a_class)
