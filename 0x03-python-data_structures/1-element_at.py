#!/usr/bin/python3
def element_at(my_list, idx):
    my_list.pop()
    if idx < 0:
        return None
    if any(x < idx for x in my_list):
        return None
