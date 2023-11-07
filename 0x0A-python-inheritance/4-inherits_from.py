#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from the
    specified class

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        bool: True if obj is an instance of a class that inherited from the
        specified class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
