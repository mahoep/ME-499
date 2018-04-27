#!usr/bin/env python3
'''
@author Matthew Hoeper
'''

def rand_sum(n):
    '''
    :param n, an integer:
    :return a list of times where each element is the amount of time it takes to sum a list:
    '''
    from numpy import random as nprandom
    from time import time
    sum_time = []
    for i in range(len(n)):
        a = nprandom.random_sample((n[i],))
        # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.random_sample.html#numpy.random.random_sample

        start_time = time()
        sum(a)
        end_time = time() - start_time
        sum_time.append(end_time)

    return sum_time
    # print("{0:.10f}".format(sort_time[i]))


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    sum_time = rand_sum(n)
    plt.semilogx(n, sum_time)
    plt.ylabel("Time (s)")
    plt.xlabel("Length of List")
    plt.show()