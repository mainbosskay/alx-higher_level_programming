#!/usr/bin/python3
"""Rectangle that defines a rectangle by: (based on 6-rectangle.py)"""


class Rectangle:
    """Class rectangle represented"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args: width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        type(self).number_of_instances += 1
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

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Printing the rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectgle = []
        for k in range(self.__height):
            [rectgle.append('#') for t in range(self.__width)]
            if k != self.__height - 1:
                rectgle.append("\n")
        return ("".join(rectgle))

    def __repr__(self):
        """Calculates and returns string representation of the rectangle"""
        rectgle = "Rectangle(" + str(self.__width)
        rectgle = rectgle + ", " + str(self.__height) + ")"
        return (rectgle)

    def __del__(self):
        """Printing the message Bye reactangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
