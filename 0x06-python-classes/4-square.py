#!/usr/bin/python3
'''Defines a square'''


class Square:
    '''Represents a square'''
    def __init__(self, size=0):
        '''Initializes a square
Args:
        size(int): the size of the square
        '''
        self.size = size
    @property
    def size(self):
        '''Get/set current size of square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Determines correct type and value of size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Returns current area of square'''
        return (self.__size * self.__size)
