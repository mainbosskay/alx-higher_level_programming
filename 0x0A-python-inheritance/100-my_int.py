#!/usr/bin/python3
"""Class MyInt that inherits from int"""


class MyInt(int):
    """Nonconformist rendition of a numerical value"""

    def __eq__(self, value):
        """Redefining equality opt to act like inequality"""
        return self.real != value

    def __ne__(self, value):
        """Redefining inequality opt to act like equality"""
        return self.real == value
