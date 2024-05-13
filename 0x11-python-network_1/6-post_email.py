#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.post(url=sys.argv[1], data={"email": sys.argv[2]})
    print(response.content.decode("utf-8"))
