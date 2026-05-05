#!/usr/bin/env python3

def pow(a, b):
    result = 1
    if b == 0:
        return result
    else:
        for i in range(b):
            result = result * a
    return result
