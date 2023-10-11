#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicc = dict(a_dictionary)
    for key in dicc:
        dicc[key] *= 2
    return dicc
