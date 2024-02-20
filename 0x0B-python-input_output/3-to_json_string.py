#!/usr/bin/python3
"""
    Here we have the module descriptions
    Functions:
        - to_json_strig(my_obj)
"""
import json


def to_json_string(my_obj):
    """Get the json representation"""
    return json.dumps(my_obj)
