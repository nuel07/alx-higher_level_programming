#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format().
        Args:
            value (int): The integer to print.
        Returns:
            If a TypeError or ValueError occurs - False.
            Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
