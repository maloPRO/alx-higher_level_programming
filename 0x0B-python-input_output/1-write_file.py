#!/usr/bin/python3

""" Writes File """


def write_file(filename="", text=""):
    """
    writes to file
    
    Args:
        filename (str): Name of file
        text(str): text to be written on file
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    return len(text)
