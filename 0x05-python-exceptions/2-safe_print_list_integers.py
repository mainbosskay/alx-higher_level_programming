#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printint = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            printint += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return (printint)
