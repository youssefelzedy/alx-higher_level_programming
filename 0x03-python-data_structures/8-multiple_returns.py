#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        typ = (len(sentence), sentence[0])
    else:
        typ = (len(sentence), "None")
    return (typ)
