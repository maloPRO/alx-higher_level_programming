#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return None
    else:
        new_tuple = (len(sentence), sentence[0].upper())
        return new_tuple