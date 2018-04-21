#!/usr/bin/env python
'''
ME 499/599 Spring 2018
A fake sensor class

Bill Smart
'''

from math import sin
from random import gauss


# Generates data from a fictional sensor, complete with measurement
# noise.
def generate_sensor_data(n=1000, noise=0.05):
	'''
	Generate data from a fictional sensor, complete with measurement noise.
	The function will return a list with n elements with additive zero-mean
	Gaussian noise, with the given standard deviation.
	'''
	return [sin(x * 0.01) + gauss(0.0, noise) for x in range(n)]


def print_sensor_data(data, filename):
	'''
	Print sensor data to a file.
	'''
	with open(filename, 'w') as f:
		for i in range(len(data)):
			f.write('{0}\t{1}\n'.format(i, data[i]))
