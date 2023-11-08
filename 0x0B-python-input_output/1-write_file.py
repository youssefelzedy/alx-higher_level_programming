#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """wirite file function"""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
