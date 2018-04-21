#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

def gcd(m, n):
    '''Returns the value of the Ackermann function'''
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return gcd(m-1, 1)
    elif m > 0 and n > 0:
        return gcd(m-1, gcd(m, n-1))

if __name__ == '__main__':
    print(gcd(3, 4))