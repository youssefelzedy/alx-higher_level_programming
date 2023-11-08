#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict of class"""
        return self.__dict__
