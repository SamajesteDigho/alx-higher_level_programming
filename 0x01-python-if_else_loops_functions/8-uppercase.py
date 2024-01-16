#!/usr/bin/python3
def uppercase(str):
    for c in str:
        l = ord(c)
        if 96 < l < 123 :
            l = l - 32
        print(f"{l:c}", end='')
    print('')
