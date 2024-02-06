#!/usr/bin/python3
"""Returns the JSON representation of an object (string)"""
from json import dumps


def to_json_string(my_obj):
    """Checks a string object and returns the JSON
    Args: my_obj (str): object of string to check"""
    return dumps(my_obj)
