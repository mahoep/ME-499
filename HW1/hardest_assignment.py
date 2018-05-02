#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def hardest_assignment(headers, data):
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