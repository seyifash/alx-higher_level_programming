#!/usr/bin/python3
"""It contains a function that returns True if the object is exactly
    an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns True if @obj is instance of @a_class, else False

    Args:
        obj (any): the object to check.
        a_class (type): the class to match thetype of obj to.
        Returns:
            True if obj is exactly an instance of the a_class else false
    """
    if type(obj) == a_class:
        return True
    return False
