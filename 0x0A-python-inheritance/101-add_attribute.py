#!/usr/bin/python3
"""Function that adds new attribute to an object"""


def add_attribute(obj, att, value):
    """AddIng new attribute to an object if it’s possible
    Args: obj (any): object to add attribute to
    att (str): name of the attribute to add to the object
    value (any): value of the attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)
