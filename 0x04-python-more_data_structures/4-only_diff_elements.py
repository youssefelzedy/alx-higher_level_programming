#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    settt = set()
    for i in set_1:
        if ((i not in set_2) and (i not in settt)):
            settt.add(i)
        else:
            continue
    for i in set_2:
        if ((i not in set_1) and (i not in settt)):
            settt.add(i)
        else:
            continue
    return settt