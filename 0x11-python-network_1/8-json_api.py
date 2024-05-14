#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = {"q": sys.argv[1]}
    else:
        data = {"q": ""}
    response = requests.post(url="http://0.0.0.0:5000/search_user", data=data)
    try:
        content = response.json()
        if content is None or len(content.keys()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(content["id"], content["name"]))
    except Exception:
        print("Not a valid JSON")
