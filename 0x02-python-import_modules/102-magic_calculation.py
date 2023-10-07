#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a > b:
        return a + b
    elif a < b:
        return a - b
    else:
        return a * b
