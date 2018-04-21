#!/usr/bin/env python

'''
ME 499/599 Spring 2018
Null filter example code.

Bill Smart
'''


def apply_null_filter(data):
	'''
	A null filter example.  This function shows the general form for a filter for this lab,
	but does not actually modify the data.
	'''
	filtered = []
	for datum in data:
		filtered.append(datum)
	return filtered


if __name__ == '__main__':
	from sensor import *

	data = generate_sensor_data()

	filtered_data = apply_null_filter(data)

	print_sensor_data(data, 'raw')
	print_sensor_data(filtered_data, 'filtered')

