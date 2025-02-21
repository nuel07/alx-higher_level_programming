#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes a square
Args:
        size(int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
