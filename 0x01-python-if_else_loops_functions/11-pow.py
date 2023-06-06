#!/usr/bin/python3

def pow(a, b):
    result = 1
    for i in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    else:
        return result
