#!/usr/bin/python3
"""
    Here the description of the module
"""


def append_after(filename="", search_string="", new_string=""):
    """Here the description of the function"""
    lines = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, x in enumerate(lines):
            if x.__contains__(search_string):
                lines.insert(i + 1, new_string)
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
