#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A subclass for the built-in list class"""

    def print_sorted(self):
        """prints a elements of a list in sorted way"""
        print(sorted(self))
