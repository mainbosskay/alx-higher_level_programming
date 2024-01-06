#!/usr/bin/python3

def no_c(my_string):
    if my_string[:]:
        newstr = my_string.translate({ord("c"): None})
        new_str = newstr.translate({ord("C"): None})
        return new_str
    return my_string
