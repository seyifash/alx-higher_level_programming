#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """A function that prints the first and last name of a person

    Args:
    first_name(str): the  first name to print.
    last__name(str): the last name to print.
    Raises:
    TypeError: if the first name of lastname is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
