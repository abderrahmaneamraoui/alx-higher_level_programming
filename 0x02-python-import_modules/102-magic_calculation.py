#!/usr/bin/python3
def magic_calculation(a, b):
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
