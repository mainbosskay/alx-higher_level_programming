#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response"""
from urllib import request, error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        try:
            with request.urlopen(urldt) as urlresp:
                print(urlresp.read().decode("utf-8"))
        except error.HTTPError as httperr:
            print(f"Error code: {httperr.code}")
