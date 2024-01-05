#!/usr/bin/python3

def no_c(my_string):
    numstr = my_string.translate({ord(ch): None for ch in'cC'})
    return numstr
