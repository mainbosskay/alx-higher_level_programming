#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element = 0
    for idx in range(x):
        try:
            print(my_list[idx], end="")
            element = element + 1
        except IndexError:
            break
        print("")
        return (element)
