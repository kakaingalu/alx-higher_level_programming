#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as reponse:
    content = reponse.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- uft8 content: {}".format(content.decode('utf-8')))
