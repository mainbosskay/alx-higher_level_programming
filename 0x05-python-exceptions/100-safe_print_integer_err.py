#!/usr/bin/python3

def safe_print_integer_err(value):
    from sys import exc_info, stderr
    try:
        print("{:d}".format(value))
        return (True)
    except TypeError:
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return (False)
    except ValueError:
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return (False)
