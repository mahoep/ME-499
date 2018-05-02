#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''
def hardest_lab(headers, data):
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