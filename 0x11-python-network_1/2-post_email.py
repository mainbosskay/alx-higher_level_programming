#!/usr/bin/python3
"""Python script that takes in a URL and an email, send a POST"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        urldt = sys.argv[1]
        email = sys.argv[2]
        encdt = bytes(parse.urlencode([("email", email)]), "utf-8")
        with request.urlopen(urldt, data=encdt) as urlresp:
            print(urlresp.read().decode("utf-8"))
