#!/usr/bin/python3
"""Class Student that defines a student"""


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

    def to_json(self):
        """Gets and returns the dictionary representation of the student"""
        return self.__dict__
