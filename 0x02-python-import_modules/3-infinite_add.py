#!/usr/bin/python3
import sys


def add():
    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print(f"{sum}")


if __name__ == "__main__":
    add()
