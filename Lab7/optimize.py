#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import numpy as np

def optimize_step(f, bounds, n):
    '''
    finds the largest value of a function, between a set of bounds
    :param f: f is the function
    :param bounds: bounds is a tuple specifying the lower (inclusive) and upper (exclusive) bounds
    :param n: n is the number of steps
    :return: returning the x value of the largest one
    '''

    low = bounds[0]
    up = bounds[1]
    f_chuncked = np.array_split(f, n)
    max_lst = []
    for i in f_chuncked:
        max_lst.append(max(i))
    value = max(max_lst)
    return value



if __name__ == '__main__':
    t = np.linspace(-1000, 1000, 10000)
    f = 3*t**2 - 18*t + 8

    bounds = (-10, 20)
    n = 25
    new = optimize_step(f, bounds, n)
    print(new)
