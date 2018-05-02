#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def final_scores(headers, data):
    import numpy as np
    for x in range(len(headers)):
        if "Final Score" == headers[x]:
            idx = x

    scores = data[1:, idx]

    avg_final_score = np.mean(scores)
    med_final_score = np.median(scores)

    above_avg = 0
    above_med = 0
    for x in scores:
        if x > avg_final_score:
            above_avg += 1
        if x > med_final_score:
            above_med += 1
    above_avg_ratio = (len(scores) - above_avg) / len(scores) * 100
    above_med_ratio = (len(scores) - above_med) / len(scores) * 100

    return [avg_final_score, above_avg_ratio, med_final_score, above_med_ratio], scores