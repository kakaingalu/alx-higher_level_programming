#!/usr/bin/python3
def multiple_returns(sentence):
    first_char= sentence[0] 
    num_of_chars = len(sentence)

    if num_of_chars == 0:
        first_char = "None"
    return num_of_chars, first_char
