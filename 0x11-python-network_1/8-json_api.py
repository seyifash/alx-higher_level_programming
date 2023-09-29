#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
a url and takes a letter as a parameter
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}

    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        data_json = r.json()
        if data_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(data_json.get("id"), data_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
