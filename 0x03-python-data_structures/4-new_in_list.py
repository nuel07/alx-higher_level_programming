#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """replaces an element in a copied list at specific index."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    
        
    myCopy = my_list.copy()
    myCopy[idx] = element
    return (myCopy)
