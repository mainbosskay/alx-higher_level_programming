#!/usr/bin/python3
"""Function that multiplies 2 matrices by using the module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Should return multiplication of two matrices in array of lists
    Args: m_a (list of lists of integers or floats): first matrix
    m_b (list of lists of integers or floats): second matrix"""
    mavaerr = "shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)"
    mbvaerr = "shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)"
    errlstma = "shapes (1,2) and (1,2) not aligned: 2 (dim 1) != 1 (dim 0)"
    errlstmb = "shapes (2,2) and (2,2) not aligned: 2 (dim 1) != 2 (dim 0)"
    if type(m_a) != list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if type(m_b) != list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError(errlstma)
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError(errlstmb)
    if m_a == [] or m_a == [[]]:
        raise ValueError(mavaerr)
    if m_b == [] or m_b == [[]]:
        raise ValueError(mbvaerr)
    if not all(len(rows) == len(m_a[0]) for rows in m_a):
        raise ValueError("setting an array element with a sequence.")
    if not all(len(rows) == len(m_b[0]) for rows in m_b):
        raise ValueError("setting an array element with a sequence.")
    for rows in m_a:
        for column in rows:
            if type(column) != int and type(column) != float:
                raise TypeError("invalid data type for einsum")
    for rows in m_b:
        for column in rows:
            if type(column) != int and type(column) != float:
                raise TypeError("invalid data type for einsum")
    return np.matmul(m_a, m_b)
