#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import numpy as np
from scipy.optimize import minimize_scalar
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

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
    i_max = 0
    for i in range(n):
        low = bounds[0]
        up = bounds[1]
        num = np.random.random_integers(low, up) + np.random.random()
        y = func(num)
        if y > max:
            max = y
            i_max = num
        else:
            pass

    return i_max


def max_scalar(f, bounds, n):
    '''
    Finds the maximum value of a funciton over an interval
    :param f: the function to be evaluated
    :param bounds: a tuple with the lower and upper x values
    :param n: the max number of iterations that the function will evaluated
    :return: the x value of the function max
    '''
    low = bounds[0]
    up = bounds[1]
    max_value = minimize_scalar(lambda x: -f(x), bounds=(low, up), method='bounded', options={'maxiter':n})
    return max_value.x


def func(x):
    # function that works well
    return -x**2 + 3*x
    # function that works poorly
    # return np.tan(x)*np.log(x)


def graph(n, method1, method2, method3):
    plt.plot(n, method1)
    plt.plot(n, method2)
    plt.plot(n, method3)
    plt.xlabel('Number of iterations')
    plt.ylabel('Error from actual value')
    plt.title('Error for Several Optimization Methods for -x**2 + 3*x over [0,5]')
    blue = mpatches.Patch(color='blue', label='Optimize_Step')
    orange = mpatches.Patch(color='orange', label='Optimize_Random')
    green = mpatches.Patch(color='green', label='Minimize_Scaler')
    plt.legend(handles=[blue, orange, green])


if __name__ == '__main__':

    bounds = (0, 5)
    n = np.linspace(1000, 100000, 20)
    answer = 1.5 # for good funciton
    # answer = -5.44073 # for bad function
    step = []
    rand = []
    builtin = []
    for i in n:
        val = int(i)
        step.append(optimize_step(func, bounds, val))
        rand.append(optimize_random(func, bounds, val))
        builtin.append(max_scalar(func, bounds, val))

    step = [abs(x - answer) for x in step]
    rand = [abs(x - answer) for x in rand]
    builtin = [abs(x - answer) for x in builtin]
    graph(n, step, rand, builtin)
    plt.show()