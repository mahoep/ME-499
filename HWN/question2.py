#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

from math import sqrt


def mysqrt(a):
    x = 0.5*a
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y


def test_square_root():
    print('a   mysqrt(a)    math.sqrt(a)   diff')
    print('-   -----------  ------------   ----')

    for i in range(1, 9):
        test = float("{0:.8f}".format(mysqrt(i)))
        actual = float("{0:.8f}".format(sqrt(i)))
        dif = float("{0:.20f}".format((abs(mysqrt(i) - sqrt(i)))))

        if len(str(test)) < 4:
            print('{}\t{}\t         {}\t        {}\t'.format(i, test, actual, dif))
        else:
            print('{}\t{}\t {}\t    {}\t'.format(i, test, actual, dif))


if __name__ == '__main__':
    test_square_root()
