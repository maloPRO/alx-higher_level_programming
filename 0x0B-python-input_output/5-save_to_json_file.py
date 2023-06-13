#!/usr/bin/python3

"""
This module contains a function that writes an
Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file

    Args:
        my_obj: object file
        filename: name of file
    """

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
