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
            norm = np.divide(data[1:, x], max(data[1:, x]))
            index[np.mean(norm)] = headers[x]
            avg.append(np.mean(norm))
    lowest = min(avg)

    return index