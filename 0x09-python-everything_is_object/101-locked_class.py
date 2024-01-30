#!/usr/bin/python3
"""Class LockedClass with no class or object attribute"""


class LockedClass:
    """Preventing user from dynamically creating new
    instance attributes"""
    __slots__ = ["first_name"]
