#!/usr/bin/python3
import urllib.request
""" a Python script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        if response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- uft8 content: {}".format(content.decode('utf-8')))
