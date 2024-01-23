#!/usr/bin/python3
"""MagicClass that does exactly the same as the bytecode given"""
from math import pi


class MagicClass:
    """Geometric circle is represented"""
    def __init__(self, radius=0):
        """Initializing the MagicClass
        Args: radius(float or init): radius of the new MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Gets and returns the area of the magicclass"""
        return (self.__radius ** 2 * pi)

    def circumference(self):
        """Gets and returns the circumference of the magicclass"""
        return (2 * pi * self.__radius)
