#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, elt in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(elt), end=' ')
            if i == len(row) - 1:
                print("{:d}".format(elt), end='')
        print('')
