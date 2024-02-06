#!/usr/bin/python3
"""Class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """Student defined is being represennted"""

    def __init__(self, first_name, last_name, age):
        """Intializing a student
        Args: first_name (str): Student first name
        last_name (str): Student last name
        age (int): Student age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets the dictionary representation of the student
        Args: attrs (list): Attributes to represent (optional)"""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """All attribure of the student being replaced
        Args: json (dict): Attributes being replaced by key/value"""
        for k, t in json.items():
            setattr(self, k, t)
