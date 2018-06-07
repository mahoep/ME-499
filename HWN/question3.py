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

        if r <= 1:
            inside += 1
        else:
            outside += 1

    mypi = inside/(inside+outside)/(circle_radius**2)
    return mypi


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    n = 25000
    print('estimate =', pi_mc(n), ' | ', 'difference =', abs(pi_mc(n)-np.pi))
    # mypi = []
    # dif = []
    # n_tests = 100
    # for i in range(n_tests):
    #     mypi.append(pi_mc(n))
    #     dif.append(pi_mc(n)-np.pi)
    #
    # plt.scatter(mypi, dif)
    # plt.axhline(y=0, color='k')
    # plt.grid()
    # plt.xlabel("Estimated value of pi")
    # plt.ylabel("Difference from built in value of pi")
    # plt.suptitle("Distribution of {} estimates of pi using Monte Carlo Integration".format(n_tests))
    # plt.title('n = {} for each estimate of pi'.format(n))
    # plt.show()