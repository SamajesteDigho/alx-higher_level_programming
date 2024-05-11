#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


data = {"email": sys.argv[2]}
data_enc = urlencode(data).encode("utf-8")
request = Request(sys.argv[1], data=data_enc, method="POST")
request.add_header("Content-Type", "application/x-www-form-urlencode")
try:
    with urlopen(request) as response:
        body = response.read()
    print(body.decode())
except Exception as e:
    print(e)