#!/usr/bin/python3
"""Read a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads and prints a text file to stdout"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
