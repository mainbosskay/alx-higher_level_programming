#!/usr/bin/python3

def magic_calculation(a, b):
    calc = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception("Too far")
            calc += a ** b / k
        except Exception:
            calc = b + a
            break
    return (calc)
