def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print("{:c}".format(ord(c) - 32), end='')
        else:
            print("{:c}".format(ord(c)), end='')
    print()
