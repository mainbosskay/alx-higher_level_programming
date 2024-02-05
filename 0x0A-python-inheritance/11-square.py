#!/usr/bin/python3
"""Class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is represented using rectangle"""

    def __init__(self, size):
        """Initializing the square
        Args: size (int): size of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculating area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Representaation of square string in an informal way"""
        return (f"[Square] {self.__size}/{self.__size}")
