#!/usr/bin/python3
"""Returning True if the object is exactly an instance
of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Checks and returns True if an objectis instance of class
    Args: obj (any): object that will be checked
    a_class (type): class to match if obj is same type"""
    if type(obj) == a_class:
        return True
    else:
        return False
