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


def evaluate(coeff, x):

    if isinstance(coeff, list) == 0:
        raise TypeError('Input must be a list')
    else:
        pass
    power = 0
    ans = 0
    for i in reversed(coeff):
        ans = i * (x**power) + ans
        power += 1
    return ans


if __name__ == '__main__':
    a = 3
    b = 4
    c = 2
    print(roots([1, 4, 4]))

    print(evaluate([1, 2, 3], 2))  # This returns the value of x^2 + 2x + 3, for x = 2
    print(evaluate([1, 2, 3], Complex(1, 2)))  # This returns the value of x^2 + 2x + 3, for x = (1 + 2i)
    print(evaluate([4, 3, 2, 1], 12))  # Evaluate 4x^3 + 3x^2 + 2x + 1, for x = 12

