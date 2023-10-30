#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """ Class that defines width of a rectangle
    Attributes:
        __width (int): width of the rectangle
    """

    def __init__(self, width=0, height=0):
        """__init__ method
            Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for __width attribute

        Returns:
            int: width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for __width attribute
            Args:
            value (int): value to be set"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for __height attribute
            Returns:
            int: height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for __height attribute
            Args:
            value (int): value to be set"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
