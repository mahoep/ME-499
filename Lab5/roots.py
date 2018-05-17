#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

from complex import Complex, sqrt


def roots(coeff):

    if isinstance(coeff, list) == 0:
        raise TypeError('Input must be a list of length 3')
    else:
        pass

    a = coeff[0]
    b = coeff[1]
    c = coeff[2]

    x1 = -b/(2*a) + sqrt(b**2 - 4*a*c)

    x2 = -b/(2*a) - (sqrt(b**2 - 4*a*c))/(2*a)

    roots = (x1, x2)

    return roots


if __name__ == '__main__':
    a = 3
    b = 4
    c = 2
    print(roots([3, 4, 2]))
