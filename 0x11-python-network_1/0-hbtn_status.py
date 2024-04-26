#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as urlreq


if __name__ == "__main__":
    with urlreq.urlopen("https://alx-intranet.hbtn.io/status") as urlres:
        if urlres.readable():
            urldata = urlres.read()
            print("Body response:")
            print(f"\t- type: {type(urldata)}")
            print(f"\t- content: {urldata}")
            print(f"\t- utf8 content: {urldata.decode('utf-8')}")
