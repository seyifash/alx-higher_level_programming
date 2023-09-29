#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    therequest = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(therequest) as response:
        thebody = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(thebody)))
        print("\t- content: {}".format(thebody))
        print("\t- utf8 content: {}".format(thebody.decode("utf-8")))
