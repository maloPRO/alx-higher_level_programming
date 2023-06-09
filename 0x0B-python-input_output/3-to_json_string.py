#!/usr/bin/python3

"""
This module contains a function that returns
the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    Converts object  to JSON

    Args:
        my_obj: string to be converted to json

    Returns:
        str: JSON rep of object
    """

    return json.dumps(my_obj, sort_keys=True)
