#!/usr/bin/python3
"""Class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Square class represented"""
    def __init__(self, size=0):
        """Initializing the square class
        Args: size (int): size of the square"""
        self.size = size

    @property
    def size(self):
        """Gets and returns the current size of the square"""
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
        """Calculates and returns the current area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Checking the == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checking the != comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checking the < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Checking the <= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checking the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checking the >= comparison"""
        return self.area() >= other.area()
