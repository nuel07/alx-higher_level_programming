#!/usr/bin/python3


def safe_print_division(a, b):
    """returns the result of dividing two integers a and b"""
    try:
        result = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        break
    finally:
        print("Inside result: {}".format(result))
    return(result)

