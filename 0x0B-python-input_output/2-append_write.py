#!/usr/bin/python3

""" Appends texttto a file """


def append_write(filename="", text=""):
    """
    Appends text

    Args:
        filename (str): name of file
        text(str): text to be appended
    """

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)

    return len(text)
