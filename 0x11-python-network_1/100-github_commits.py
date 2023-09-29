#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user rails
"""
import sys
import requests


if __name__ == "__main__":
    theurl = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                                 sys.argv[1])
    r = requests.get(theurl)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
