#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    reslt = 0
    for k in range(len(argv) - 1):
        reslt = reslt + int(argv[k + 1])
    print("{}".format(reslt))
