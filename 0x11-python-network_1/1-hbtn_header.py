#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
from urllib.request import urlopen


if len(sys.argv) > 1:
    with urlopen(sys.argv[1]) as response:
        id = response.headers["X-Request-Id"]
    print(id)
