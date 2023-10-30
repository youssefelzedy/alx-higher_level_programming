#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """ Class that defines width of a rectangle
    Attributes:
        __width (int): width of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ method
            Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)

    def __str__(self):
        """Method that returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        return string[: -1]

    def __repr__(self):
        """Method that returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method that deletes an instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle based on the area
            Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
            Returns:
            Rectangle: biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Method that returns a new Rectangle
        instance with width == height"""
        return cls(size, size)
