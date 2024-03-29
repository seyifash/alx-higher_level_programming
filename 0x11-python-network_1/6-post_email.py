#!/usr/bin/python3
"""script that takes in a URL and an email address,
sends a POST request to the passed URL
"""
import sys
import requests


if __name__ == "__main__":
    theurl = sys.argv[1]
    email = sys.argv[2]

    r = requests.post(theurl, data={'email': email})
    print(r.text)
