#!/usr/bin/env python3

def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = ord(letter) - 32
            letter = chr(letter)
        print("{}".format(letter), end="")

    print()
