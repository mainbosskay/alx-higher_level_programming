#!/usr/bin/python3

k = 0
for t in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(t - k)), end="")
    k = 32 if k == 0 else 0
