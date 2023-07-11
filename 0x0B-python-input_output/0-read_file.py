#!/usr/bin/python3
"""Opens a file a nd reads from a file"""


def read_file(filename=""):
    """reads a text file (UTF-8) and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(). end="")
