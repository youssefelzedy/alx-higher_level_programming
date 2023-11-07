#!/usr/bin/python3
"""Module for BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes a BaseGeometry object"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of a Rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
