#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Printing sorted list of builtin list class"""

    def print_sorted(self):
        """Printing list from class in sorted ascending order"""
        print(sorted(self))
