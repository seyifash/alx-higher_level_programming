#!/usr/bin/python3
"""Contains the BaseGeometry class"""


class BaseGeometry:
    """A baseclass geometry"""

    def area(self):
        """computes the area of this geometry"""
        raise Exception("area() is not implemented")
