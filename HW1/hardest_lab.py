#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''
def hardest_lab(headers, data):
    '''
        Calculates the most difficult lab in grades.csv based on lowest average
        :requires a list with the headers from the csv file
        :requires a numpy array with all of the data from csv file
        :returns lab with lowest average
        '''
    import numpy as np
    index = {}
    avg = []
    for x in range(len(headers)):
        if "Lab" in headers[x] and "Quiz" not in headers[x] and "Score" not in headers[x]:
            v = data[:, x]
            v = v[~np.isnan(v)]
                #https://stackoverflow.com/questions/19852586/get-mean-value-avoiding-nan-using-numpy-in-python?
            norm = np.divide(v, max(v))
            index[np.mean(norm)] = headers[x]
            avg.append(np.mean(norm))
    lowest = min(avg)

    return index[lowest]