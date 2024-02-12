#!/usr/bin/python3
"""
    The N queens game player programming
"""
from sys import argv, stderr

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N", file=stderr)
        exit(1)
    try:
        N = int(argv[1])
    except Exception:
        print("N must be a number", file=stderr)
        exit(1)
    if N < 4:
        print("N must be at least 4", file=stderr)
        exit(1)
    print("N is {:d}".format(N))
