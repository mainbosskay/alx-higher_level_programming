#!/usr/bin/python3
"""Class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Attributes: __size (int): size of square"""
    def __init__(self, size=0):
        """Methods: __init__(self, size=0): Initializing new square
        instance with the specified size
        Args: size (init): Size of new square. Default is 0
        Raises: TypeError: If the provided size is not an integer
        ValueError: If the provided size less than 0"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
