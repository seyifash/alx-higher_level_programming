#!/bin/bash
# script that takes in a URL, sends a GET request to the URL

status_code=$(curl -L -s -X HEAD "$1" | grep -i "HTTP" | cut -d " " -f 2)

if [ "$status_code" -eq 200 ];
then
	curl -Ls "$1"
fi
