#!/usr/bin/python3

def safe_function(fct, *args):
    from sys import stderr
    try:
        funcsafe = fct(*args)
    except Exception as execerror:
        print("Exception: {}".format(execerror), file=stderr)
        return None
    else:
        return funcsafe
