#!/usr/bin/python3
import json

""" serialize to json string """


def to_json_string(my_obj):
    """
    Converts string to JSON

    Args:
        my_obj (str): string to be converted to json
    """

    json_data = json.dumps(my_obj)

    return json_data
