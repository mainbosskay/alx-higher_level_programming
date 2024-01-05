#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for k in matrix:
        for t in k:
            print("{:d}".format(t), end=" " if t != k[-1] else "")
        print()
