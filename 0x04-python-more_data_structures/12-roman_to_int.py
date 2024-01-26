#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    cpy = "{}.".format(roman_string)
    cvt = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    res = []
    if roman_string:
        for i, x in enumerate(cpy):
            if x == ".":
                res.append(0)
            elif x == "I" and cpy[i+1] in 'XV':
                res.append(-cvt[x])
            elif x == "X" and cpy[i+1] in 'CL':
                res.append(-cvt[x])
            elif x == "C" and cpy[i+1] in 'MD':
                res.append(-cvt[x])
            else:
                res.append(cvt[x])
    return sum(res)
