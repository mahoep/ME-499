#!usr/bin/env python3
'''
@author Matthew Hoeper
'''

def rand_samp(n):
    '''
    :param n, an integer:
    :return a list of numbers of n length where each element is the sum of 10 random numbers:
    '''
    from numpy import random as nprandom
    u = []
    for i in range(n):
        v = nprandom.random_sample(10,)
        # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.uniform.html
        u.append(sum(v))
    return u

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    t = rand_samp(10000)
    plt.hist(t)
    plt.ylabel("Number of Occurrences")
    plt.xlabel("Sum of 10 random Numbers")
    plt.show()