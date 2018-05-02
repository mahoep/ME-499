#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def grade_cutoff(scores):
    from numpy import percentile
    #https://stackoverflow.com/questions/2374640/how-do-i-calculate-percentiles-with-python-numpy?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

    dist = [90, 70, 40, 10]
    cutoff = []
    for x in dist:
        cutoff.append(round(percentile(scores, x),2))

    return cutoff

