#!/usr/bin/python3

def max_integer(my_list=[]):
    if type(my_list) is list:
        if not my_list:
            return None
        else:
            max_int = 0

            for i in my_list:
                if i > max_int:
                    max_int = i
            return max_int
