#!/usr/bin/python3
"""
    Here the documentation of the module
"""
from urllib.request import urlopen


with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode("utf-8")))
