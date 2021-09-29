#!/usr/bin/python3


def magic_calculation(a, b):
    """performs a magical calculation"""
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            else:
                res += a ** b / i
        except:
            res = b + a
            break
    return (res)
