#!/usr/bin/python3

import json
""" 
This module contains a function
that converts an object  to json string
"""

def to_json_string(my_obj):
    """
    Converts object  to JSON

    Args:
        my_obj: string to be converted to json

    Returns:
        str: JSON rep of object
    """

    return json.dumps(my_obj, sort_keys=True)
