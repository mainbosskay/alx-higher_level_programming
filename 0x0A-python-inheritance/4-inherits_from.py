#!/usr/bin/python3
"""Checking if object is instance or inherit from a class"""


def inherits_from(obj, a_class):
    """Checks and returns True if object is instance of a class
    Args: obj (any): object that will be checked
    a_class (type): class to match if the object is of same type"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
