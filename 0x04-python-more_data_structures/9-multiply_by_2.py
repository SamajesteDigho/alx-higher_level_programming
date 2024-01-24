#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    if a_dictionary:
        for k in a_dictionary.keys():
            res[k] = a_dictionary[k] * 2
    return res
