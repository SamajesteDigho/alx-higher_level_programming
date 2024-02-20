#!/usr/bin/python3
"""
    Here we have the module descriptions
    Functions:
        - save_to_json_file(my_obj, filename)
"""
import json


def save_to_json_file(my_obj, filename):
    """From json to string"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
