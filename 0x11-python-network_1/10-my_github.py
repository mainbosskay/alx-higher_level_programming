#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        urldt = "https://api.github.com/user"
        username = sys.argv[1]
        password = sys.argv[2]
        api_headers = {
                "Accept": "application/vnd.github.v3+json",
                "Username": username,
                "Authorization": f"token {password}"
        }
        urlresp = requests.get(urldt, headers=api_headers)
        urlstatus = urlresp.status_code
        if urlstatus == 200:
            github_user = urlresp.json()
            if github_user["login"] == username:
                print(github_user["id"])
            else:
                print("None")
        else:
            print("None")
