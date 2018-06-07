#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import numpy as np

def rand_prop(n = 100000):

    yes = 0
    no = 0
    for i in range(n):

        num1 = np.random.uniform(0, 1)
        num2 = np.random.uniform(0, 1)
        if num1 < num2:
            yes += 1
        else:
            no += 1

    p = yes/(yes+no)
    return p


if __name__ == '__main__':
    print('The probability that one random number is less than a second random number is: {}'.format(rand_prop()))


