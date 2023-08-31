#!/usr/bin/bash

# Takes a URL, sends request and displays

url=$1
response=$(curl -s -o /dev/null -w "%{size_download}" "$url")
echo $response
