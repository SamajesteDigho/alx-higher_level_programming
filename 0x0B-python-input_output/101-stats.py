#!/usr/bin/python3
"""
    Here the description of the module
"""
import sys


if __name__ == "__main__":
    count = -1
    status = {}
    size = 0
    for x in sys.stdin:
        count += 1
        data = x.strip().split(" ")
        if data[-1].isnumeric():
            size += int(data[-1])
            if data[-2] in status.keys():
                status[data[-2]] += 1
            else:
                status[data[-2]] = 1
        if count % 10 == 0 and count > 0:
            print("File size: {}".format(size))
            keys = list(status.keys())
            keys.sort()
            for key in keys:
                print("{}: {}".format(key, status[key]))
    print("File size: {}".format(size))
    keys = list(status.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, status[key]))
