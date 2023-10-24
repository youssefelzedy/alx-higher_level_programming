#!/usr/bin/python3
"""class Square"""


class Square:

    """ init class """

    def __init__(self, size=0, position=(0, 0)):

        """init
        Args:
            size (int): size of square
        Position:
            position (tuple): position of square
        """

        self.__size = size
        self.__position = position

    """ getter """

    @property
    def size(self):
        """size getter"""
        return (self.__size)

    """ setter """

    @size.setter
    def size(self, value):
        """
        size setter
        Args:
            value (int): size of square
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    """ getter """

    @property
    def position(self):
        """position getter"""
        return (self.__position)

    """ setter """

    @position.setter
    def position(self, value):
        """
        position setter
        Args:
            value (int): size of square
        """
        if all(isinstance(num, int) and num >= 0 for num in value):
            self.__position = value
            return
        raise TypeError("position must be a tuple of 2 positive integers")

    """ area """

    def area(self):
        """area"""
        return (self.__size ** 2)

    """ print """

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
