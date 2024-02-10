#!/usr/bin/python3
"""Defining rectangle class inherited from base"""
from models.base import Base


class Rectangle(Base):
    """Defined rectangle is being represented"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle class
        Args: width (int): rectangle's width
        height (int): rectangles's height
        x (int): x-coordinate of the rectangle
        y (int): y-coordinate of the rectangle
        id (int): rectangle's identifier"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets and returns rectangles width"""
        return (self.__width)

    @width.setter
    def width(self, dig):
        """Setting the rectangle width"""
        if type(dig) is not int:
            raise TypeError("width must be an integer")
        if dig <= 0:
            raise ValueError("width must be > 0")
        self.__width = dig

    @property
    def height(self):
        """Gets and returns rectangles height"""
        return (self.__height)

    @height.setter
    def height(self, dig):
        """Setting the rectangle height"""
        if type(dig) is not int:
            raise TypeError("height must be an integer")
        if dig <= 0:
            raise ValueError("height must be > 0")
        self.__height = dig

    @property
    def x(self):
        """Gets and returns x coordnate of the rectangle"""
        return (self.__x)

    @x.setter
    def x(self, dig):
        """Setting the x coordinate of the rectangle"""
        if type(dig) is not int:
            raise TypeError("x must be an integer")
        if dig < 0:
            raise ValueError("x must be >= 0")
        self.__x = dig

    @property
    def y(self):
        """Gets and returns y coordinate of the rectangle"""
        return (self.__y)

    @y.setter
    def y(self, dig):
        """Setting the y coordinate of the rectangle"""
        if type(dig) is not int:
            raise TypeError("y must be an integer")
        if dig < 0:
            raise ValueError("y must be >= 0")
        self.__y = dig

    def area(self):
        """Calculates and returns area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Printing the rectangle using the # char"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """Calculates and returns rectangles string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument and key/value argument to attributes
        Args: *args (int): Added attribute values
            1st argument representing the id attribute
            2nd argument representing the width attribute
            3rd argument represnting the height attribute
            4th argument represnting the x attribute
            5th argumnet represnting the y attribute
        **kwargs (dict): Added key/value attributes"""
        if args and len(args) != 0:
            arg = 0
            for ags in args:
                if arg == 0:
                    if ags is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = ags
                elif arg == 1:
                    self.width = ags
                elif arg == 2:
                    self.height = ags
                elif arg == 3:
                    self.x = ags
                elif arg == 4:
                    self.y = ags
                arg = arg + 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """generates the dictionary representation of the rectangle"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })
