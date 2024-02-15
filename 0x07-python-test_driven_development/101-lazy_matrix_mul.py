#!/usr/bin/python3
"""
    Module for numpy matrix multiplication
    functions:
        lazy_matrix_mul(m_a, m_b)
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Matrix multiplication using numpy module
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(elt, list) for elt in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(elt, list) for elt in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if any(not isinstance(elt, (int, float)) for row in m_a for elt in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(elt, (int, float)) for row in m_b for elt in row):
        raise TypeError("m_b should contain only integers or floats")
    col_a = set(len(row) for row in m_a)
    if len(col_a) != 1:
        raise TypeError("each row of m_a must be of the same size")
    col_b = set(len(row) for row in m_b)
    if len(col_b) != 1:
        raise TypeError("each row of m_b must be of the same size")
    size_a = (len(m_a), list(col_a)[0])
    size_b = (len(m_b), list(col_b)[0])
    if size_a[1] != size_b[0]:
        raise ValueError("m_a and m_b can't be multiplied")
    result = np.dot(np.matrix(m_a), np.matrix(m_b))
    return result.tolist()
