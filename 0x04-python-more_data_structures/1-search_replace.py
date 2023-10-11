#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lisst = []
    for i in my_list:
        if i == search:
            lisst.append(replace)
        else:
            lisst.append(i)
    return lisst
