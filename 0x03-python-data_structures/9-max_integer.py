#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    cpy = my_list.copy()
    cpy.sort(reverse=True)
    return cpy[0]
