#!/bin/bash
# Takes a URL, sends request and displays
curl -s $1 | wc -c
