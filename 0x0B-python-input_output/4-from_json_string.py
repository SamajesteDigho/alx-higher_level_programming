#!/usr/bin/python3
"""
    Here we have the module descriptions
    Functions:
        - from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """From json to string"""
    return json.loads(my_str)
