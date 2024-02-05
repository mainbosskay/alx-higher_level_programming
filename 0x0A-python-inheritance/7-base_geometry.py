#!/usr/bin/python3
"""Class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Defined basegeometry"""

    def area(self):
        """Area of a basegeometry that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Chacks and validates parameter as integer
        Args: name (str): name of the parameter
        value (int): parameter to be validated"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
