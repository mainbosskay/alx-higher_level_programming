#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
(task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle being represented using BaseGeometry"""

    def __init__(self, width, height):
        """Initializing the rectangle
        Args: width (int): width of the rectangle
        height (int): height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculating the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Representation print() and str() of the rectangle is informal"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
