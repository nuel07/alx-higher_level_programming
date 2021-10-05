#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init_(self, width=0, height=0):
        """Initializes the rectangle
Args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise VaueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/set height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstnace(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes and returns area of the rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """Computes and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2))
