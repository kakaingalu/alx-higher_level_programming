#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ Checks if the list has any value if so it returns max"""
    # check if list has any value
    if not list_of_integers:
        return None

    # initialize left to 0 and right the length of list - 1
    left, right = 0, len(list_of_integers) - 1
    # loop through the list using its length
    while left < right:
        peak = (left + right) // 2  # peak is initialized by half of length
        if list_of_integers[peak] < list_of_integers[peak + 1]:
            left = peak + 1
        else:
            right = peak
    return list_of_integers[left]
