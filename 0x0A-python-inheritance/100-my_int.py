#!/usr/bin/python3
"""Module for BaseGeometry class"""


calss MyInt(int):
    """MY ITN CLASS"""

    def __eq__(self, other):
        """Returns the opposite of the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns the opposite of the != operator"""
        return super().__eq__(other)
