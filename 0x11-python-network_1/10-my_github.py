#!/usr/bin/python3
"""a Python script that takes in a URL, sends arequest to\
        the URL and displays the body of the response."""

import requests
import sys
if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                            headers={'Accept': 'application/vnd.github.v3+json'
                                     }, auth=(sys.argv[1], sys.argv[2]))
    json_dict = response.json()
    print(json_dict.get('id') if response.status_code == 200 else None)
