#!/usr/bin/python3
"""
    Here we have the module descriptions
"""
import sys, os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
if __name__ == "__main__":
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("[]")
    elements = load_from_json_file(filename)
    arguments = sys.argv[1:]
    elements.extend(arguments)
    save_to_json_file(elements, filename)
