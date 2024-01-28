#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of
these characters: ., ? and :"""


def text_indentation(text):
    """Args: text (str): text to print
    Error to raise:
    TypeError: if text is not a string"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    currentidx = 0
    while currentidx < len(text) and text[currentidx] == ' ':
        currentidx += 1
    while currentidx < len(text):
        print(text[currentidx], end="")
        if text[currentidx] == "\n" or text[currentidx] in ".?:":
            if text[currentidx] in ".?:":
                print("\n")
            currentidx += 1
            while currentidx < len(text) and text[currentidx] == ' ':
                currentidx += 1
            continue
        currentidx += 1
