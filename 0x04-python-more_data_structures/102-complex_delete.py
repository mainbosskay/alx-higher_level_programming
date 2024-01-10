#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    delete = []
    for k, t in a_dictionary.items():
        if t == value:
            delete.append(k)
    for k in delete:
        a_dictionary.pop(k)
    return a_dictionary
