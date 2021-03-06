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
    return x**3+2


if __name__ == '__main__':

    bounds = (0, 1)
    n = np.linspace(5000, 200000, 25)
    n = [int(x) for x in n]
    area = []
    diff = []
    area_actual = 2.25
    for i in n:
        ans = integrate_mc(func, bounds, i)
        area.append(ans)
        diff.append(abs(area_actual-ans))
    plt.plot(n, diff)
    plt.grid()
    plt.xlabel('Number of Samples')
    plt.ylabel('Error from Actual Value')
    plt.title('Error vs. Number of Samples for Monte Carlo Integration of x**3+2 over [0,1]')
    plt.show()
    # print(area)
