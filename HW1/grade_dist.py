#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def grade_dist(scores):
    a = 0
    a_minus = 0
    b_plus = 0
    b = 0
    b_minus = 0
    c_plus = 0
    c = 0
    c_minus = 0
    d_plus = 0
    d = 0
    d_minus = 0
    f = 0

    for x in scores:
        if x > 94:
            a = a + 1
        elif x < 90 and x > 94:
            a_minus = a_minus + 1
        elif x < 90 and x > 87:
            b_plus = b_plus + 1
        elif x < 87 and x > 84:
            b = b + 1
        elif x < 84 and x > 80:
            b_minus = b_minus + 1
        elif x < 80 and x > 77:
            c_plus = c_plus + 1
        elif x < 77 and x > 74:
            c = c + 1
        elif x < 74 and x > 70:
            c_minus = c_minus + 1
        elif x < 70 and x > 67:
            d_plus = d_plus + 1
        elif x < 67 and x > 64:
            d = d + 1
        elif x < 64 and x > 61:
            d_minus = d_minus + 1
        else:
            f = f + 1

    grades = [a, a_minus, b_plus, b, b_minus, c_plus, c, c_minus, d_plus, d, d_minus, f]

    return grades
