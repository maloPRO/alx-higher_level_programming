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

    obj_class = type(obj)

    if obj_class is not a_class and issubclass(obj_class, a_class):
        return True

    for base_class in a_class.__bases__:
        if inherits_from(obj, base_class):
            return True

    return False
