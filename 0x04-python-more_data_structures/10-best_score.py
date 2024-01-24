#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    score = 0
    if a_dictionary:
        for k in a_dictionary.keys():
            if a_dictionary[k] > score:
                best = k
                score = a_dictionary[k]
    return best
