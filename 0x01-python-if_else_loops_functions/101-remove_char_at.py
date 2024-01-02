#!/usr/bin/python3

def remove_char_at(str, n):
    if n >= 0:
        kstr = str[:n] + str[n + 1:]
        return (kstr)
    else:
        return (str)
