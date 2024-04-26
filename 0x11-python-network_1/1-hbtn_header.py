#!/usr/bin/python3
"""Python script that takes, send a request and displays URL"""
import urllib.request as urlreq
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        with urlreq.urlopen(urldt) as urlres:
            print(urlres.headers["X-Request-Id"])
