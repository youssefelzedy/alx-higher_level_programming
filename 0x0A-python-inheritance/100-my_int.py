#!/usr/bin/python3
"""Module for BaseGeometry class"""


calss MyInt(int):
    """MY ITN CLASS"""

    def __eq__(self, value):
        """Returns the opposite of the == operator"""
        return int(self) != value

    def __ne__(self, value):
        """Returns the opposite of the != operator"""
        return int(self) == value
