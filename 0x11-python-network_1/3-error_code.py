#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
manage urllib.error.HTTPError exceptions and print: Error code
"""
import urllib.request
import sys


if __name__ == "__main__":
    theurl = sys.argv[1]
    try:
        with urllib.request.urlopen(theurl) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
