#!/usr/bin/python3
"""Writing an Object to a text file, as a JSON representation"""
from json import dump


def save_to_json_file(my_obj, filename):
    """Using JSON represntation to write an object to text file"""
    with open(filename, "w") as fl:
        dump(my_obj, fl)
