#!/usr/bin/python3
"""4-print_square module"""


def print_square(size):
    """Prints a square with the character #.
        Args:
            size (int): size of the square
        Returns:
            None
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    [print("#" * size) for i in range(size)]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
