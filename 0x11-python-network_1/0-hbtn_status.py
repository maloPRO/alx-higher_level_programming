#!/usr/bin/python3
# Write a Python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:

        response_content_bytes = response.read()

        response_content_utf8 = response_content_bytes.decode('utf-8')

        print("Body response:")
        print(f"\t- type: {type(response_content_bytes)}")
        print(f"\t- content: {response_content_bytes}")
        print(f"\t- utf8 content: {response_content_utf8}")
