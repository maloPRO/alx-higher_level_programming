#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        new_tuple = (len(sentence), sentence[0].upper())
    else:
        return None
    return new_tuple
