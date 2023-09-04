#!/usr/bin/python3
# Write a Python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print(body)
