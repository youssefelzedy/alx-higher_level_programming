#!/usr/bin/python3

"""Module for is_same_class method"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) == a_class
