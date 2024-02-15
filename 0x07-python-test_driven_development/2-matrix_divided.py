#!/usr/bin/python3
"""
    Here is the module for the exercise 2-matrix_divided
    functions:
        matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
        This function permits to divide each element of a matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers"
                        + "/floats")
    if not all(isinstance(elt, list) for elt in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers"
                        + "/floats")
    if any(not isinstance(elt, (int, float)) for row in matrix for elt in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers"
                        + "/floats")
    if len(set([len(x) for x in matrix])) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for i, row in enumerate(matrix):
        result.append([])
        for elt in row:
            result[i].append(round(elt / div, 2))
    return result
