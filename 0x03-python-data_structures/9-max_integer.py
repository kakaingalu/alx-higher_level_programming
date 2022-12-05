#!/usr/bin/python3
def max_integer(my_list=[]):
    counter = len(my_list)
    if counter == 0:
        return (None)
    else:
        max_n = my_list[0]
        for i in range(counter):
            if my_list[i] > max_n:
                max_n = my_list[i]
        return max_n
