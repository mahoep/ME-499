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
    x = np.linspace(low, up, 10000)
    y = f(x)
    y_chuncks = np.array_split(y, n)
    max_lst = []
    idx_lst = []
    for i in y_chuncks:
        max_lst.append(max(i))
        idx_lst.append(np.argmax(i))
    max_chunk = np.argmax(max_lst)
    max_idx = idx_lst[max_chunk]
    x_max = len(y_chuncks[0])*(max_chunk) + max_idx

    return x[x_max]


def func(x):
    return -x**2

if __name__ == '__main__':

    bounds = (-10, 10)
    n = 25
    new = optimize_step(func, bounds, n)
    print(new)
