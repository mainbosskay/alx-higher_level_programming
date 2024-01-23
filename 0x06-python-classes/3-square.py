#!/usr/bin/python3
"""Class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Attributes: __size (int): Size of the square"""
    def __init__(self, size=0):
        """Methods: __init__(self, size=0): Initializing new square
        with specified size
        Args: size (int): Size of the new square, default is 0
        Raises:
        TypeError: If the provided size is not an integer
        ValueError: If the provided size is less than 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area(self): Calculate and return current area
        of the square"""
        return (self.__size * self.__size)
