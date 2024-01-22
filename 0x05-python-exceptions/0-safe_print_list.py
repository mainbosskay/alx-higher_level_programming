#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        element = 0
        for k in range(0, x):
            try:
                print("{}".format(my_list[k]), end="")
                element += 1
            except (IndexError):
                continue
        print()
        return element
