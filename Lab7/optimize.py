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
    :return: returning the x value of the largest x value where max occurs
    '''

    low = bounds[0]
    up = bounds[1]
    x = np.linspace(low, up, n)
    y = f(x)
    x_idx = np.argmax(y)

    return x[x_idx]


def optimize_random(f, bounds, n):
    '''
    finds the largest value of a function, between a set of bounds
    :param f: f is the function
    :param bounds: bounds is a tuple specifying the lower (inclusive) and upper (exclusive) bounds
    :param n: n random samples between the bounds
    :return: returning the x value of the largest x value where max occurs
    '''

    max = 0
    for i in range(n):
        low = bounds[0]
        up = bounds[1]
        num = np.random.random_integers(low, up) + np.random.random()
        y = func(num)
        if y > max:
            max = num
        else:
            pass

    return max


def func(x):
    return -x**2


if __name__ == '__main__':

    bounds = (-5, 5)
    n = 2500
    # step = optimize_step(func, bounds, n)
    # print(new)
    rand = optimize_random(func, bounds, n)
    print(rand)