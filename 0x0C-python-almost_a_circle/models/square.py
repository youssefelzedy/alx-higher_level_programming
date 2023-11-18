#!/usr/bin/python3
"""Square class"""
import os.path
import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class
        Args:
            size (int): size of the square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): id of the square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))
