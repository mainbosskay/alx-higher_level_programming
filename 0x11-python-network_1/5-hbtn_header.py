#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the variable"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        urlresp = requests.get(urldt)
        if "X-Request-Id" in urlresp.headers:
            print(urlresp.headers["X-Request-Id"])
