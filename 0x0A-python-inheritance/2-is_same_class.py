#!/usr/bin/python3

""" checks if object is instance of a class """


def is_same_class(obj, a_class):
    """
    Chcks if object is instance af a_class

    Args:
        obj (object): object to be checked
        a_class (object): class to be checked

    Returns:
        bool: True or false
    """

    return type(obj) is a_class
