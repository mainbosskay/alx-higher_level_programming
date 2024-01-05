#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    numlist = []
    for k in my_list:
        numlist.append(k)
    if idx < 0 or idx >= len(my_list):
        return numlist
    else:
        numlist[idx] = element
        return numlist
