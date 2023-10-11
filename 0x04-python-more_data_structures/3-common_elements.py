#!/usr/bin/python3
def common_elements(set_1, set_2):
    settt = set()
    for i in set_1:
        if ((i in set_2) and (i not in settt)):
            settt.add(i)
        else:
            continue
    return settt
