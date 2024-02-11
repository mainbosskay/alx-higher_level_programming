#!/usr/bin/python3
"""Base of all other classes in this project"""
import csv
import json
import turtle


class Base:
    """Defined base being represented
    Private class attribute:
    __nb_objects (int): Sum of created base instances"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base class
        Args: id (int): New base instance identifier"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize and returns list of dict to JSON string
        Args: list_dictionaries (list): dictionaries to serialize"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Serialize and write list of objects to file as JSON string
        Args: list_objs (list): instances gotten from the base class"""
        flname = cls.__name__ + ".json"
        with open(flname, "w") as jsonfl:
            if list_objs is None:
                jsonfl.write("[]")
            else:
                lst_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfl.write(Base.to_json_string(lst_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Deserialize and returns JSON string to python list
        Args: json_string (str): list of dicts represented by JSON string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Instantiates and returns a class from dict of attributes
        Args: **dictionary (dict): Attributes to initialize are key/value"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                nwinst = cls(1, 1)
            else:
                nwinst = cls(1)
            nwinst.update(**dictionary)
            return (nwinst)

    @classmethod
    def load_from_file(cls):
        """Class instance from JSON file loads and returns a list instance"""
        flname = str(cls.__name__) + ".json"
        try:
            with open(flname, "r") as jsonfl:
                lst_dicts = Base.from_json_string(jsonfl.read())
                return [cls.create(**dct) for dct in lst_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and write to file as CSV list of objects
        Args: list_objs (list): list of instances gotten from base class"""
        flname = cls.__name__ + ".csv"
        with open(flname, "w", newline="") as classfl:
            if list_objs is None or list_objs == []:
                classfl.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                clwriter = csv.DictWriter(classfl, fieldnames=fieldnames)
                for objtinst in list_objs:
                    clwriter.writerow(objtinst.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Class instance from CSV file loads and returns list instance"""
        flname = cls.__name__ + ".csv"
        try:
            with open(flname, "r", newline="") as classfl:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                lst_dicts = csv.DictReader(classfl, fieldnames=fieldnames)
                lst_dicts = [dict([key, int(val)] for key, val in dct.items())
                             for dct in lst_dicts]
                return [cls.create(**dct) for dct in lst_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Using imported turtle module to draw rectangles and squares
        Args: list_rectangles (list): rectangles list to draw
        list_squares (list): squares list to draw"""
        turtcol = turtle.Turtle()
        turtcol.screen.bgcolor("#808080")
        turtcol.pensize(2)
        turtcol.register_shape("heart", ((-30, -40), (0, 40), (30, -40)))
        turtcol.shape("heart")

        turtcol.color("#8F9779")
        for rect in list_rectangles:
            turtcol.showturtle()
            turtcol.up()
            turtcol.goto(rect.x, rect.y)
            turtcol.down()
            for side in range(2):
                turtcol.forwars(rect.width)
                turtcol.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turtcol.hideturtle()

        turtcol.color("4682B4")
        for sqre in list_squares:
            turtcol.showturtle()
            turtcol.up()
            turtcol.goto(sqre.x, sqre.y)
            turtcol.down()
            for side in range(4):
                turtcol.forward(sqre.width)
                turtcol.left(90)
            turtcol.hideturtle()
        turtle.exitonclick()
