#!/usr/bin/python3
""" a Python script that takes in a URL and an email,\
        sends a POST request to the passed URL with the\
        email as a parameter, and displays the body \
        of the response (decoded in utf-8) """
import requests
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    response = requests.post(argv[1], data=data)
    print(response.text)
