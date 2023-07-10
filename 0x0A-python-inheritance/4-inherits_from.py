#!/usr/bin/python3
"""Contains a function that tests if an object inherits from a class"""


def inherits_from(obj, a_class):
    """returns True if @obj is an instance of a class that inherited
    from @a_class (directly or indirectly)

    Args:
    obj (any): The objct to check.
    a_class (type): The class to match the type of obj to.
    Returns:
    if obj is an inherited of a_class -True
    otherwise -False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
