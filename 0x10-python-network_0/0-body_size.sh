#!/usr/bin/bash
# Takes a URL, sends request and displays
echo $(curl -s -o /dev/null -w "%{size_download}" "$1")
