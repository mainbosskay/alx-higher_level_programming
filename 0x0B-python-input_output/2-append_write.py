#!/usr/bin/python3
"""Appends a string at the end of a text file (UTF8) and
returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTFB text file
    Args: filename (str): filename to append the string to
    text (str): string to append to the file"""
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
