#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
import requests


if __name__ == "__main__":
    name = sys.argv[1]
    pswd = sys.argv[2]

    header = {
        "Accept: application/vnd.github+json"
    }
    data = {
        "access_token": "{}".format()
    }