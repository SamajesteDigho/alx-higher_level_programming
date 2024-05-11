#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
from urllib.request import urlopen, Request
from urllib.error import HTTPError


try:
    with urlopen(sys.argv[1]) as response:
        body = response.read()
    print("{}".format(body.decode("utf-8")))
except HTTPError as e:
    print("Error code: {}".format(e.code))
