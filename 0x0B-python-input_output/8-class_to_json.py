#!/usr/bin/python3

"""
This module contains a function that returns the
dictionary description with simple data structure
"""

import json


def class_to_json(obj):
    """
    Gets dict desc
    """
    if isinstance(obj, (list, tuple)):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {class_to_json(key): class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, (int, bool)):
        return obj
    elif hasattr(obj, '__dict__'):
        return class_to_json(obj.__dict__)
    else:
        return None
