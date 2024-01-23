#!/usr/bin/python3
"""Class Square that defines a square by: (based on 6-square.py)"""


class Square:
    """Square class represented"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the square class
        Args: size (int): size of square
        position (int, int): Position of the square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets and returns the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setting the square position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(digit, int) for digit in value) or
                not all(digit >= 0 for digit in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square in # char"""
        if self.__size == 0:
            print("")
            return
        for k in range(self.__position[1]):
            print("")
        for t in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square"""
        if self.__size == 0:
            return ""
        reslt = ""
        for k in range(self.__position[1]):
            reslt += "\n"
        for t in range(self.__size):
            reslt += " " * self.__position[0] + "#" * self.__size + "\n"
        return reslt[:-1]
