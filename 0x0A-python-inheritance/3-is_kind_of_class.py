#!/usr/bin/python3
"""Checking if object is an instance or inherits from a class"""


def is_kind_of_class(obj, a_class):
    """Checks and returns True if object is instance of a class
    Args: obj (any): object that will be checked
    a_class (type): class to match if object is of same class type"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
