#!/usr/bin/python3
""" a Python script that fetches \
        https://alx-intranet.hbtn.io/status """

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status").text
    if response:
        cont = response
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
