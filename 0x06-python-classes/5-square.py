#!/usr/bin/python3
"""Class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Square class represented"""
    def __init__(self, size):
        """Initializing the square class
        Args: size (int): Size of the square"""
        self.size = size

    @property
    def size(self):
        """Gets and returns current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setting the square size"""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square in # char"""
        for k in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
