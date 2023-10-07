#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        arr = []
        if (idx < 0):
            arr = my_list
            return (my_list)
        if (idx > len(my_list)):
            arr = my_list
            return (my_list)
        for i in range(len(my_list)):
            if (i == idx):
                arr.append(element)
            arr.append(my_list[i])
        return (arr)
