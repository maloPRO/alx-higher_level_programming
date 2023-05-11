#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        operators = ("+", "-", "/", "*")

        if operator in operators:
            if operator == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif operator == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif operator == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            elif operator == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
