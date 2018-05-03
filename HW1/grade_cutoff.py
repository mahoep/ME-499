#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def grade_cutoff(scores):
    '''
        Calculates the grade cutoff marks based on
        10% get an A, 20% get a B, 30% get a C, 30% get a D, and the rest get an F
        :requires a list with the final scores
        :returns grade cutoff for A,B,C,D
        '''
    from numpy import percentile
    #https://stackoverflow.com/questions/2374640/how-do-i-calculate-percentiles-with-python-numpy?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

    dist = [90, 70, 40, 10]
    cutoff = []
    for x in dist:
        cutoff.append(round(percentile(scores, x),2))

    return cutoff

