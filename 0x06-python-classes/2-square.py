#!/usr/bin/python3
"""class Square"""


class Square:
    """init class"""
    def __init__(self, size=0):
        """size init"""
        try:
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
        else:
            pass