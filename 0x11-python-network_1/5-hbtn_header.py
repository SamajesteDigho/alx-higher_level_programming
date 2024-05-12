#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get("{}".format(sys.argv[1]))
    print("{}".format(response.headers["X-Request-Id"]))
