#!/usr/bin/python3
""" Peak finder module """


def find_peak(list_of_integers):
    """ Finding the pick out of the list"""
    ls = list_of_integers
    ls.reverse()
    if len(ls) == 0:
        return None
    if 0 < len(ls) < 3:
        return ls[0]
    i = 1
    while i < len(ls) - 1:
        if ls[i-1] <= ls[i] >= ls[i+1] or ls[i-1] >= ls[i] <= ls[i+1]:
            return ls[i]
        i += 1
    return ls[i]
