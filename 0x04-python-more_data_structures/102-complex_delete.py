#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in range(len(a_dictionary)):
        if i == value:
            del a_dictionary[i]
    return a_dictionary
