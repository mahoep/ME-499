#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

import math as m
def estimate_pi():
    '''Returns an estimation of pi'''
    k = 0
    inf_sum = 0
    while 1:
        const = (2 * m.sqrt(2))/9801
        inf_sum = inf_sum + m.factorial(4*k) * (1103 + 26390*k) / (m.factorial(k)**4 * 396**(4*k))
        pi = 1/(const*inf_sum)
        k += 1
        if abs(pi - m.pi) < 1e-15:
            break
    return pi

if __name__ == '__main__':

    print(estimate_pi()-m.pi)