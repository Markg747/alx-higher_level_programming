#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ch = ord(c)
        if ch >= 97 and ch <= 122:
            ch -= 32
        print("{:c}".format(ch), end="")
    print()
