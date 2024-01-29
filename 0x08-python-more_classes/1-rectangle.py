#!/usr/bin/python3
"""Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """Class rectangle represented"""
    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args: width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets and returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets and returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
