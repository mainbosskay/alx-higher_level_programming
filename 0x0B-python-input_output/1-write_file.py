#!/usr/bin/python3
"""Write a string to a text file (UTF8) and returns
the number of characters written"""


def write_file(filename="", text=""):
    """Writing a string to UTFB text file
    Args: filename (str): filename to write
    text (str): text to be writte into the file"""
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
