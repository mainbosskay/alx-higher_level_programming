#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    romandict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    figure = 0
    for dig in range(len(roman_string)):
        if dig > 0 and romandict[roman_string[dig]] > romandict[roman_string[dig - 1]]:
            figure += romandict[roman_string[dig]] - 2 * \
                        romandict[roman_string[dig - 1]]
        else:
            figure += romandict[roman_string[dig]]
    return figure
