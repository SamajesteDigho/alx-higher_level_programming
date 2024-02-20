#!/usr/bin/python3
"""
    Here we have the module descriptions
    Functions:
        - load_from_json_file(filename)
"""
import json


def load_from_json_file(filename):
    """Load from json file"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        return json.loads(content)
