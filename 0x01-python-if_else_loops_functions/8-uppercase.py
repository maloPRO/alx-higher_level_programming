#!/usr/bin/python3

def uppercase(str):
    result = ""
    for i in str:
        if (ord(i) < 123 and ord(i) > 96):
            result += "{}".format(chr(ord(i) - 32))
        else:
            result += "{}".format(i)
    print(result + "\n", end="")
