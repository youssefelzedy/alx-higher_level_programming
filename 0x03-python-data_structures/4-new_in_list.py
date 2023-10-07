#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    arr = []
    if (idx < 0):
        return (my_list)
    if (idx > len(my_list)):
        return (my_list)
    for i in range(len(my_list)):
        if (i == idx):
            arr.append(element)
        arr.append(my_list[i])
    return (arr)
