#!/usr/bin/python3
"""Contains a function that tests for kind of class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from the specified
    class, otherwise False

    Args:
        obj (any): The object to check.
        a_class (type): the class to match the type of obj to

    Returns:
        if obj is an instance or inherited instance of a_class - True
        otherwise false
    """
    return isinstance(obj, a_class)
