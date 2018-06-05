#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import numpy as np
from scipy.optimize import minimize_scalar
from matplotlib import pyplot as plt

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


def max_scalar(f, bounds, n):
    low = bounds[0]
    up = bounds[1]
    max_value = minimize_scalar(lambda x: -f(x), bounds=(low, up), method='bounded', options={'maxiter':n})
    return max_value


def func(x):
    return np.sin(x)


def grapher():
    max = 0
    max_real = 1
    error = []
    n_val = np.linspace(0, 24999, 25000)

    for i in range(n):
        low = bounds[0]
        up = bounds[1]
        num = np.random.random_integers(low, up) + np.random.random()
        y = func(num)
        error.append(abs(max_real - y))
        if y > max:
            max = num
        else:
            pass
    plt.plot(n_val,error)
    plt.show()



if __name__ == '__main__':

    bounds = (-5, 5)
    n = 25000
    # step = optimize_step(func, bounds, n)
    # print(new)
    # rand = optimize_random(func, bounds, n)
    # print(rand)
    # builtin = max_scalar(func, bounds, n)
    # print(builtin)
    # grapher()