#!/usr/bin/python3
""" A script that sends a request to the URL and displays the response body
 HTTP status code is greater than or equal to 400, print: Error code
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
