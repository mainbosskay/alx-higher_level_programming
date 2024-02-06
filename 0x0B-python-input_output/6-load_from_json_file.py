#!/usr/bin/python3
"""Creating an Object from a JSON file"""
from json import load


def load_from_json_file(filename):
    """Create a python object with a JSON file"""
    with open(filename) as fl:
        return load(fl)
