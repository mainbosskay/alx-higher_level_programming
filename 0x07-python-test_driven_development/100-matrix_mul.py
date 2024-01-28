#!/usr/bin/python3
"""Function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """Args: m_a (list of lists if ints/floats): first matrix
    m_b (list of listsof ints/floats): second matrix
    Errors to raise:
    TypeError: 1. if m_a or m_b is not a list
                2. if m_a or m_b is not a list of lists
                3. if m_a or m_b is not an integer or float
                4. if m_a or m_b has different sized rows
    ValueError: 1. if m_a or m_b is empty
                2. if m_a or m_b cannot be multiplies"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError("m_b must be a list of lists")
    for rows in m_a:
        for column in rows:
            if type(column) != int and type(column) != float:
                raise TypeError("m_a should contain only integers or floats")
    for rows in m_b:
        for column in rows:
            if type(column) != int and type(column) != float:
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(rows) == len(m_a[0]) for rows in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(rows) == len(m_b[0]) for rows in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    transposed = []
    for matrow in range(len(m_b[0])):
        noeqrow = []
        for currentidx in range(len(m_b)):
            noeqrow.append(m_b[currentidx][matrow])
        transposed.append(noeqrow)

    newmat = []
    for rows in m_a:
        noeqrow = []
        for col in transposed:
            result = 0
            for k in range(len(transposed[0])):
                result += rows[k] * col[k]
            noeqrow.append(result)
        newmat.append(noeqrow)
    return newmat
