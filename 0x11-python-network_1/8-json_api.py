#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    urldt = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        urlquery = sys.argv[1]
    else:
        urlquery = ""
    encdt = [("q", urlquery)]
    urlresp = requests.post(urldt, data=encdt)
    try:
        jsondt = urlresp.json()
        if jsondt:
            print(f"[{jsondt['id']}] {jsondt['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
