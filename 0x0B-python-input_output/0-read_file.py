#!/usr/bin/python3

""" Opens file """


def read_file(filename=""):
    """
    Opens and reads a file

    Args:
        filename (str): Filename
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
