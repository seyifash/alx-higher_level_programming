#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the
    number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        no_of_chars = f.write(text)
        return no_of_chars
