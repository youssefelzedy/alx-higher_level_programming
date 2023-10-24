#!/usr/bin/python3
"""class Square"""


class Square:

    """ init class """

    def __init__(self, size=0):

        """init
        Args:
            size (int): size of square
        """

        self.__size = size

    """ getter """

    @property
    def size(self):
        """size getter"""
        return (self.__size)

    """ setter """

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    """ area """

    def area(self):
        """area"""
        return (self.__size ** 2)
