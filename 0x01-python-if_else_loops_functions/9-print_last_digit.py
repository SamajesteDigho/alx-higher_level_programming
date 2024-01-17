#!/usr/bin/python3
def print_last_digit(number) -> int:
    last = number % 10 if number >= 0 else 10 - number % 10
    print(f"{last}", end='')
    return last
