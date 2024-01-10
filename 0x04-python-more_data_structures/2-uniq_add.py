#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqlist = set(my_list)
    figure = 0
    for num in uniqlist:
        figure = figure + num
    return (figure)
