#!/usr/bin/python3
# Write a Python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')
print(body)
