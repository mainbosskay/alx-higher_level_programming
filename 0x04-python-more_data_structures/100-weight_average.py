#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    fig = 0
    digit = 0
    for num in my_list:
        fig = fig + num[0] * num[1]
        digit = digit + num[1]
    return (fig / digit)
