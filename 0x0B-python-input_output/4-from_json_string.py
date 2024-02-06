#!/usr/bin/python3
"""Returning an object represented by a JSON string"""
from json import loads


def from_json_string(my_str):
    """Checks and returns a python object represnted by a JSON string
    Args: my_str (str): JSON string being checked"""
    return loads(my_str)
