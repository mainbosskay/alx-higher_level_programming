#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        github_repo = sys.argv[1]
        github_user = sys.argv[2]
        base_url = "https://api.github.com"
        commits_url = (
                f"{base_url}/repos/{github_user}/{github_repo}/"
                f"commits?per_page=10"
        )
        urlresp = requests.get(
                commits_url,
                headers={"Accept": "application/vnd.github.v3+json"}
        )
        urlstatus = urlresp.status_code
        if urlstatus == 200:
            for commit in urlresp.json():
                SHA_commit = commit["sha"]
                author_name = commit["commit"]["author"]["name"]
                print(f"{SHA_commit}: {author_name}")
