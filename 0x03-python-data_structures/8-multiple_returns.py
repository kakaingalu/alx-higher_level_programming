#!/usr/bin/python3
def multiple_returns(sentence):
    num_of_chars = len(sentence)
    if num_of_chars == 0:
        first_char = "None"
    else:
        first_char = sentence[0]
    return num_of_chars, first_char
