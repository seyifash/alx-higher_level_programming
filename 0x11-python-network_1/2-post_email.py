#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL
"""
import urllib.request
import sys


if __name__ == "__main__":
    theurl = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values).encode('ascii')
    with urllib.request.urlopen(theurl, data=data) as response:
        print(response.read().decode('utf-8'))
