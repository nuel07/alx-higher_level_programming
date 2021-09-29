#!/usr/bin/python3

import sys


def safe_functions(fct, *args):
    """executes a function safely"""
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exceptiono: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
