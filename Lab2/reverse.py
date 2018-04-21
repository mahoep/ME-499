#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''


def reverse_i(list):
    '''Returns the reverse of a list'''
    rev = []
    for x in range(0, len(list)):
        rev.append(list[-x-1])
    return rev


def reverse_r(list):
    '''Returns the reverse of a list recursively'''
    if len(list) == 1:
        return list
    else:
        return [list[-1]] + reverse_r(list[:-1])


if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd', 'e']
    b = [1, 2, 3, 4, 5, 6]
    print(reverse_i(a))
    print(reverse_i(b))

    print(reverse_r(a))
    print(reverse_r(b))