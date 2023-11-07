#!/usr/bin/python3
"""Module for is_same_class method"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj: object to look up

    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)
