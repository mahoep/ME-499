#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import numpy as np
import matplotlib.pyplot as plt


def integrate_mc(f, bounds, n):
    '''
    Monte Carlo integration approximation
    Reference: http://mathworld.wolfram.com/MonteCarloIntegration.html
    :param f: function to be "integrated"
    :param bounds: bounds of integration
    :param n: number of random samples
    :return: approximation of integration, float
    '''

    xlow = bounds[0]
    xup = bounds[1]
    x = np.linspace(xlow, xup, 10000)
    y = f(x)
    ylow = 0
    yup = np.max(y)

    area_box = (xup - xlow)*(yup - ylow)

    under = 0
    above = 0
    for i in range(n):
        xrand = np.random.uniform(xlow, xup)
        yrand = np.random.uniform(ylow, yup)
        if yrand <= f(xrand):
            under += 1
        else:
            above += 1

    area = under/(under+above)*area_box
    return area

def func(x):
    return x


if __name__ == '__main__':

    bounds = (0, 1)
    n = 250000

    area = integrate_mc(func, bounds, n)
    print(area)
