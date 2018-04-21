#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

from sensor import *
import numpy as np

data = generate_sensor_data(n=1000, noise=0.05)

def mean_filter(data, width):
    mean_data = []
    for x in range(0, len(data)-width+1):
        avg = sum(data[x:x+width-1])/width
        mean_data.append(avg)
    return mean_data

def median_filter(data, width):
    median_data = []
    for x in range(0, len(data) - width + 1):
        median = np.median(data[x:x+width-1])
        median_data.append(median)
    return median_data


if __name__ == '__main__':

    data_new_mean = mean_filter(data,3)
    data_new_median = median_filter(data,3)

    for i,datum in enumerate(data_new_mean):
        print(i, datum)

    for i, datum in enumerate(data_new_median):
        print(i, datum)









