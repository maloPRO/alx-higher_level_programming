#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) < 123 and ord(i) > 96):
            print("{}".format(chr(ord(i) -32)), end="")
        else:
            print("{}".format(i), end="")
