#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            cyp_list = my_list.copy()
            cyp_list[idx] = element
            return cyp_list
