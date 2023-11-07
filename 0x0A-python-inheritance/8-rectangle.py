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
