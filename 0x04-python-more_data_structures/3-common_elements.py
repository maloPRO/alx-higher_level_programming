#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = filter(lambda item: item in set_2, set_1)
    return next(common, None)
