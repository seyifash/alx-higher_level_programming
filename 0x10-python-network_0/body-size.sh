#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [[ $# -ne 0 ]]
then
	theurl="$1"
	curl -s -o response.tmp "theurl"
	size=$(wc -c < response.tmp)

	echo "$size"
	rm -f response.tmp
fi
