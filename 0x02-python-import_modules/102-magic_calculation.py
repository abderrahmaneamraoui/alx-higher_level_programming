#!/usr/bin/paython3
def magic_calculation(a, b):
    add = lambda x, y: x + y
    sub = lambda x, y: x - y

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
