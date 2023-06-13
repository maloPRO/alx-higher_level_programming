#!/usr/bin/python3

"""
This script adds all arguments to a Python list
"""

import sys
import json

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
argList = load_from_json('add_item.json')

argList += args

save_to_json(argList, 'add_item.json')
load_from_json('add_item.json')
