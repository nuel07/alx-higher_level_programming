#!/usr/bin/python3
"""Defines a rectangle with dimensions"""



class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle 
Args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    """Get/set height of the rectangle"""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
