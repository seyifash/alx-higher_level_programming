#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the size of a square
        Args:
        size(int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current squaere area"""
        return (self.__size * self.__size)
