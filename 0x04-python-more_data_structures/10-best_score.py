#!/usr/bin/python3
def best_score(a_dictionary):
    mx = -99999
    key = -1
    for i in a_dictionary:
        if a_dictionary[i] > mx:
            mx = a_dictionary[i]
            key = i
    return key
