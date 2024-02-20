#!/usr/bin/python3
"""
    Here the description of the module
"""


def pascal_triangle(n):
    """Here the description of the function"""
    res = []
    if n > 0:
        res = [[1]]
        for i in range(1, n):
            row = [1]
            for x in range(1, i):
                row.append(res[i-1][x-1] + res[i-1][x])
            row.append(1)
            res.append(row)
    for line in res:
        print("{}".format(line))
