#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import numpy as np


def pi_mc(n):
    circle_radius = 1/2
    inside = 0
    outside = 0
    for i in range(n):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        r = np.sqrt(x**2 + y**2)

        if r < 1:
            inside += 1
        else:
            outside += 1

    mypi = inside/(inside+outside)/(circle_radius**2)
    return mypi


def func(x, y):
    return np.sqrt(x**2 + y**2)


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    n = 250000
    # mypi = []
    # for i in range(100):
    #     mypi.append(pi_mc(n))
    #
    # plt.hist(mypi)
    # plt.show()