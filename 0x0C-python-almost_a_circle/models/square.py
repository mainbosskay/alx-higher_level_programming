#!/usr/bin/python3
"""Square class inherited from rectangle class is defined"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defined Square is being represented"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the square class
        Args: size (int): Square size
        x (int): x coordinate of the square
        y (int): y coordinate of the square
        id (int): square identifier"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets and returns the square size"""
        return (self.width)

    @size.setter
    def size(self, dig):
        """Setting the square size"""
        self.width = dig
        self.height = dig

    def __str__(self):
        """Calculates and returns the square string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assigns argument and key/value argument to the attributes
        Args: *args (int): Added attribute values
            1st argument representing the id attribute
            2nd argument representing the size attribute
            3rd argument represnting the x attribute
            4th argument represnting the y attribute
        **kwargs (dict): Added key/value attributes"""
        if args and len(args) != 0:
            arg = 0
            for ags in args:
                if arg == 0:
                    if ags is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = ags
                elif arg == 1:
                    self.size = ags
                elif arg == 2:
                    self.x = ags
                elif arg == 3:
                    self.y = ags
                arg = arg + 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Generates the square dictionary representation"""
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        })
