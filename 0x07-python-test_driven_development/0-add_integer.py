#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):

    """Add two integers
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        int: The return      value. a + b
    """
    if type(a) not in (float, int):
        raise TypeError('a must be an integer')

    if type(b) not in (float, int):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
