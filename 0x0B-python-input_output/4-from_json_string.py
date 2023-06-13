#!/usr/bin/python3

import json

""" JSON to string """


def from_json_string(my_str):
    """
    Convertsjson to string

    Args:
        my_str(str): json string
    """
    return json.loads(my_str)
