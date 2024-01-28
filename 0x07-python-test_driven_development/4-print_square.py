#!/usr/bin/python3
"""Functions that prints square with the character #"""


def print_square(size):
    """Args: size (int): height and width of the square
    Error to Raise: TypeError: 1. if size is not an integer
                                2.if size is a float and less than 0
    ValueError: if size is less than 0"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for k in range(size):
        [print("#", end="") for t in range(size)]
        print("")
