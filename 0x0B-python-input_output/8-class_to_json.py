#!/usr/bin/python3
"""Returning the dictionary description with simple data structure"""


def class_to_json(obj):
    """Checks and returns the dictionary representation of data structure"""
    return obj.__dict__
