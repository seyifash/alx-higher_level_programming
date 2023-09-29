#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    theurl = sys.argv[1]

    with urllib.request.urlopen(theurl) as response:
        x_request = response.headers['X-Request-Id']
        print(x_request)
