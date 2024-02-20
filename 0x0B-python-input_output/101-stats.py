#!/usr/bin/python3
"""
    Here the description of the module
"""
import sys


count = 0
status = {}
size = 0
for x in sys.stdin:
    count += 1
    if count % 10 == 0:
        print("File size: {}".format(size))
        for key in status.keys():
            print("{}: {}".format(key, status[key]))
    data = x.strip().split(" ")
    size += int(data[-1])
    if data[-2] in status.keys():
        status[data[-2]] += 1
    else:
        status[data[-2]] = 1
