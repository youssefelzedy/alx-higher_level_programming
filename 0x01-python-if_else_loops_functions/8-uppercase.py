#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str = str.replace(str[i], chr(ord(str[i]) - 32))
    print("{}".format(str))
