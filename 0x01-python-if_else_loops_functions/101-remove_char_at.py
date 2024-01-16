#!/usr/bin/python3
def remove_char_at(str, n) -> str:
    res = ''
    for x in range(len(str)):
        if x != n:
            res += str[x]
    return res

