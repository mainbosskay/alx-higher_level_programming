#!/usr/bin/python3
"""Class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Attributes: __size (int);the size of the square side"""
    def __init__(self, size):
        """Methods: __init__(self, size): initializing new square
        instance with the specified size
            Args:
                size (int): Size of new square"""
        self.__size = size
