#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request\
        to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        json_dict = response.json()
        if json_dict:
            print("[{}] {}".format(json_dict.get('id'), json_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
