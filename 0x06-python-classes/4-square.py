#!/usr/bin/python3
"""Class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Square class represented"""
    def __init__(self, size=0):
        """Initializing the square class
        Args: size (int): Size of the square"""
        self.size = size

    @property
    def size(self):
        """Gets and returns the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setting the square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of square"""
        return (self.__size * self.__size)
