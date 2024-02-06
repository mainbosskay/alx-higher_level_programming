#!/usr/bin/python3
"""Defining the Pascal's Triangle"""


def pascal_triangle(n):
    """Representing the defined pascal triangle
    Args: n: triangle size"""
    if n <= 0:
        return []
    pascaltri = [[1]]
    while len(pascaltri) != n:
        ptri = pascaltri[-1]
        temp = [1]
        for k in range(len(ptri) - 1):
            temp.append(ptri[k] + ptri[k + 1])
        temp.append(1)
        pascaltri.append(temp)
    return pascaltri
