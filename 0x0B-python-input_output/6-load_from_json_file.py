#!/usr/bin/python3

"""
This module contains a funtion that
creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    Creates object from json file

    Args:
        filename: name of file

    Returns:
        None
    """

    with open(filename, 'w', encoding='utf-8') as f:
        data = json.load(f)
    return data
