#!/usr/bin/python3
"""Base class"""
import os.path
import json

class Base:
    """Base class"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Base Class
        Args:
            id (int): id of the object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
