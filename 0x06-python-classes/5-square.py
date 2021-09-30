#!/usr/bin/python3
'''Defines a square'''


class Square:
    '''Represents a square'''
    def __init__(self, size=0):
        '''Initializes square
Args:
        size(int): The size of the square
        '''
        self.size = size

    @property
    def size(self):
        '''Get/set current size of the square'''
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''Return current area of the square'''
        return (self.___size * self._size)

    def my_print(self):
        '''Print square with # character'''
        for i in range(0, slef._size):
            [print('#', end="") for x in range(self._size)]
            print("")
        if self.__size == 0:
            print("")
