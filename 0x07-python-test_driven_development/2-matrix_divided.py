#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix_divided: Initializing function
    Args: matrix (list): matrix to be divided, represented
    as a list of lists
    div (int or float): divisor number used
    Errors to raise: TypeError: 1. for non-list matrix
                                2. for unequal matrix rows size
                                3. for non-numeric divisor
    ZeroDivisionError: When divisor is zero"""
    matrixsz = [0, 0]
    functionres = []
    lst_err = "matrix must be a matrix (list of lists) of integers/floats"
    matrixrow_err = "Each rows of the matrix must have the same size"
    if not isinstance(matrix, list):
        raise TypeError(lst_err)
    matrixsz[0] = len(matrix)
    if matrixsz[0] == 0:
        raise TypeError(lst_err)
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(lst_err)
        elif len(rows) == 0:
            raise TypeError(lst_err)
        else:
            if matrixsz[1] == 0:
                matrixsz[1] = len(rows)
            elif len(rows) != matrixsz[1]:
                raise TypeError(matrixrow_err)
            for columns in rows:
                if not isinstance(columns, (int, float)):
                    raise TypeError(lst_err)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for rows in matrix:
            rowsreslt = list(map(lambda t: round(t / div, 2), rows))
            functionres.append(rowsreslt)
        return functionres
