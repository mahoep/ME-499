#!usr/bin/env python3
'''
@author Matthew Hoeper
'''

def rand_sort(n):
    '''
    :param n, an integer:
    :return a list of times where each element is the amount of time it takes to sort a list:
    '''
    from numpy import random as nprandom
    from time import time
    sort_time = []
    for i in range(len(n)):
        a = nprandom.random_sample((n[i],))
        # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.random_sample.html#numpy.random.random_sample

        start_time = time()
        sorted(a)
        end_time = time() - start_time
        sort_time.append(end_time)

    return sort_time
    # print("{0:.10f}".format(sort_time[i]))


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    sort_time = rand_sort(n)
    plt.plot(n, sort_time)
    plt.ylabel("Time (s)")
    plt.xlabel("Length of List")
    plt.show()