#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''


def sum_i(list):
    '''Returns the summation of a list of numbers'''
    num_sum = 0
    for x in range(0, len(list)):
        num_sum = num_sum + list[x]

    return num_sum

def sum_r(list):
    '''Returns the summation of a list of numbers via recursion'''
    if len(list) > 0:
        num_sum = list[0] + sum_r(list[1:])
    elif len(list) == 1:
        return list[0]
    else:
        return 0

    return num_sum


if __name__ == '__main__':

    l = [3, 2, 1]
    s = sum_i(l)
    print(s)

    s = sum_r(l)
    print(s)