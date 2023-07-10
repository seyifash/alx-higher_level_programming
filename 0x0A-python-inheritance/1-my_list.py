#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """implements the printing of a sorted list for the built in list class"""
    def print_sorted(self):
        """prints a elements of a list in sorted way"""
        print(sorted(self))
