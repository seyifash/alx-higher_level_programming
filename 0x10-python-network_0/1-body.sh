#!/bin/bash
# script that takes in a URL, sends a GET request to the URL
if [ "$(curl -L -s -X HEAD -w "%{http_code}" "$1")" -eq 200 ]; then curl -Ls "$1"; fi
