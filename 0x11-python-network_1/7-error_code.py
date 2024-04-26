#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        urlresp = requests.get(urldt)
        urlstatus = urlresp.status_code
        if urlstatus >= 400:
            print(f"Error code: {urlstatus}")
        else:
            print(urlresp.text)
