#!/usr/bin/python3

def multiple_returns(sentence):
    multuple = ()
    if len(sentence) == 0:
        multuple = 0, "None"
    else:
        multuple = len(sentence), sentence[0]
    return multuple
