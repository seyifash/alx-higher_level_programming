#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response

status_code=$(curl -Ls -X HEAD "$1" | grep -i "HTTP" | cut -d " " -f 2)
if [[ "$status_code" -eq 200 ]];
then
	curl -Ls "$1"
fi	
