def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        del(my_list[idx])
    return my_list
