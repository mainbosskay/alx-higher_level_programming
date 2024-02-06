#!/usr/bin/python3
"""Inserting a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing a specific string
    Args: filename (str): filename
    search_string (str): string being searched for in the file
    new_string (str): string to insert"""
    txt = ""
    with open(filename) as fln:
        for ln in fln:
            txt += ln
            if search_string in ln:
                txt += new_string
    with open(filename, "w") as wl:
        wl.write(txt)
