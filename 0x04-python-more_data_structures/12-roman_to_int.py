#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    romandt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    indec = [romandt[num] for num in roman_string]
    figure = 0
    for dig in range(len(indec)):
        figure += indec[digit]
        if indec[digit - 1] < indec[digit] and digit != 0:
            figure -= (indec[digit - 1] + indec[digit - 1])
    return figure
