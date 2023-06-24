#!/usr/bin/python3

"""
This module contains a function that returns the
dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Gets dict desc
    """
    return obj.__dict__
