#!/usr/bin/python3
"""
    Here the documentation of the module
"""
import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == "__main__":
    # data = {"email": sys.argv[2]}
    # data_enc = urlencode(data).encode("utf-8")
    url = "{}?email={}".format(sys.argv[1], sys.argv[2])
    request = Request(url, method="POST")
    # request.add_header("Content-Type", "application/x-www-form-urlencode")
    try:
        with urlopen(request) as response:
            body = response.read()
        print(body.decode())
    except Exception as e:
        print("{}".format(e))
