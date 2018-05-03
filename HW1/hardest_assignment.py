#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def hardest_assignment(headers, data):
    '''
    Calculates the most difficult homework assignment in grades.csv based on lowest average
    :requires a list with the headers from the csv file
    :requires a numpy array with all of the data from csv file
    :returns assignment with lowest average
    '''
    import numpy as np
    index = {}
    avg = []
    for x in range(len(headers)):
        if "Homework" in headers[x] and "Final" not in headers[x] and "Current" not in headers[x]:
            v = data[:, x]
            v = v[~np.isnan(v)]
            norm = np.divide(v, max(v))
            index[np.mean(norm)] = headers[x]
            avg.append(np.mean(norm))
    lowest = min(avg)

    return index[lowest]
