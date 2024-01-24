#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    if my_list:
        sop = sum(map(lambda x: x[0] * x[1], my_list))
        under = sum(map(lambda x: x[1], my_list))
        weight = sop / under
    return weight
