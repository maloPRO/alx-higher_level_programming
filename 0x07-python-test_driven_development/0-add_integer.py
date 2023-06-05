#!/usr/bin/python3

""" 
0-add_integer.py

Adds two integers 

Functions:
    add_integer(a, b=98)

"""

def add_integer(a, b=98):

    """
    Adds 2 integers

    Args:
        a(int): first integer
        b(int): second integer

    Returns:
        int: sum of a and b

    Raises:
        ValueError: If either a or b is not an integer or float
    """

    if not isinstance(b, int) and not isinstance(b, float):
        raise ValueError("b must be an integer")
    elif not isinstance(a, int) and not isinstance(a, float):
        raise ValueError("a must be an integer")

    return int(a) + int(b)
