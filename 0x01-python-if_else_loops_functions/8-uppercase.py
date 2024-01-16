#!/usr/bin/python3
def uppercase(str):
    for car in str:
        letter = ord(car)
        if 96 < letter < 123:
            letter = letter - 32
        print(f"{letter:c}", end='')
    print('')
