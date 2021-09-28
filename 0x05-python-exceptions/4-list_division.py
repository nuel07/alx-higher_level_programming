#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""
    new_list = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("A division by zero error occurred")
            res = 0
        except TypeError:
            print("Invalid types")
            res = 0
        except IndexError:
            print("Out of list range")
            res = 0
        finally:
            new_list.append(res)
    return (new_list)
