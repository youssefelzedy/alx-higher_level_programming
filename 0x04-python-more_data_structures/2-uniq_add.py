#!/usr/bin/python3
def uniq_add(my_list=[]):
    lisst = []
    sm = 0
    for i in my_list:
        if i in lisst:
            continue
        else:
            lisst.append(i)
            sm += i
    return sm
