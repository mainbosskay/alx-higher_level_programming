#!/usr/bin/python3
"""Function that prints my first and last name"""


def say_my_name(first_name, last_name=""):
    """Args: first_name (str): first name to print
    last_name (str, optional): last name to print
    Error to raise:
    TypeError: for non-string for either first_name or last_name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
