#!/usr/bin/python3
"""Module for BaseGeometry class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initializes a BaseGeometry object"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """Returns the area of a rectangle"""
        return self.__size ** 2
