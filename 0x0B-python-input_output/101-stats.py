#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
from sys import stdin

flsize = 0
k = 0
stat_cds = {"200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for ln in stdin:
        token = ln.split()
        if len(token) >= 2:
            t = k
            if token[-2] in stat_cds:
                stat_cds[token[-2]] += 1
                k += 1
            try:
                flsize += int(token[-1])
                if t == k:
                    k += 1
            except FileNotFoundError:
                if t == k:
                    continue
        if k % 10 == 0:
            print(f"File size: {flsize:d}")
            for key, value in sorted(stat_cds.items()):
                if value:
                    print(f"{key:s}: {value:d}")
    print(f"File size: {flsize:d}")
    for key, value in sorted(stat_cds.items()):
        if value:
            print(f"{key:s}: {value:d}")

except KeyboardInterrupt:
    print(f"File size: {flsize:d}")
    for key, value in sorted(stat_cds.items()):
        if value:
            print(f"File size: {flsize:d}")
