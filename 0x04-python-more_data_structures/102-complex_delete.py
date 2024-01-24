#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys = []
        for x in a_dictionary.keys():
            if a_dictionary[x] == value:
                keys.append(x)
        for k in keys:
            del a_dictionary[k]
    return a_dictionary
