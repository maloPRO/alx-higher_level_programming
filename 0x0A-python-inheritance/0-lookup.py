#!/usr/bin/python3

""" Gets objects of a class """

def lookup(obj):
    """
    Returns methods and attributes

    Args:
        obj (object): object 

    Returns:
        list: list of methods and attributes
    
    Raises:
        TypeError: If obj is not a class
    """
    return dir(obj)
