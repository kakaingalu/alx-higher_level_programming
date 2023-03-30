#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sXI OPTIONS "$1" -o /dev/null -w "%{allow}\n'

