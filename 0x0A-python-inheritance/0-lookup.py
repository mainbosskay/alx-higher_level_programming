#!/usr/bin/python3
"""Returning the list of available attributes and methods
of an object"""


def lookup(obj):
    """Gets and returns the list of available attributes and methods"""
    return (dir(obj))
