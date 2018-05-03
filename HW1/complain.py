#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def complain(scores):
    '''
        Calculates the number of students that are within 0.5% of the next grade up
        :requires a list with the final scores
        :returns number of students that are within 0.5% of the next grade up
    '''
    num_complain = 0
    for x in scores:
        if 94 - x <= 0.5 and 94 - x > 0:
            num_complain += 1
        elif 90 - x <= 0.5 and 90 - x > 0:
            num_complain += 1
        elif 87 - x<= 0.5 and 87 - x > 0:
            num_complain += 1
        elif 84 - x <= 0.5 and 84 - x > 0:
            num_complain += 1
        elif 80 - x <= 0.5 and 80 - x > 0:
            num_complain += 1
        elif 77 - x <= 0.5 and 77 - x > 0:
            num_complain += 1
        elif 74 - x <= 0.5 and 74 - x > 0:
            num_complain += 1
        elif 70 - x <= 0.5 and 70 - x > 0:
            num_complain += 1
        elif 67 - x <= 0.5 and 67 - x > 0:
            num_complain += 1
        elif 64 - x <= 0.5 and 64 - x > 0:
            num_complain += 1
        elif 61 - x <= 0.5 and 61 - x > 0:
            num_complain += 1

    return num_complain
