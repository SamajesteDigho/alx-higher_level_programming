#!/usr/bin/python3
def print_last_digit(number) -> int:
    l = number % 10 if number >= 0 else 10 - number % 10
    print(f"{l}", end='')
    return l
