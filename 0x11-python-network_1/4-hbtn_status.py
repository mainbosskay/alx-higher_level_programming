#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    urlresp = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(urlresp.text)}")
    print(f"\t- content: {urlresp.text}")
