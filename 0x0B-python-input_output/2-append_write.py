#!/usr/bin/python3
"""Writes a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the
    number of characters appended"""
    with open(filename, "a", encoding="utf-8") as f:
        no_of_chars = f.write(text)
        return no_of_chars
