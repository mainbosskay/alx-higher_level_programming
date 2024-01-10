#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    romandict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    indec = [romandict[num] for num in roman_string]
    figure = 0
    for dig in range(len(indec)):
        figure = figure + indec[dig]
        if indec[dig - 1] < indec[dig] and dig != 0:
            figure = figure - (indec[dig - 1] + indec[dig - 1])
    return figure
