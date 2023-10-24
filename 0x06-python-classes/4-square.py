#!/usr/bin/python3
"""class Square"""


class Square:
    """ init class """

    def __init__(self, size=0):
        """init
        Args:
            size (int): size of square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    """ area """

    def area(self):
        """area"""
        return (self.__size ** 2)
        
    """ getter """

    @property
    def size(self):
        """size getter"""
        return (self.__size)

    """ setter """

    def size(self, value):
        """setter
        Args:
            size (int): size of square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
