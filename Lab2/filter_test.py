#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

from sensor import *
from null_filter import *

data = generate_sensor_data(n=1000, noise=0.05)
print_sensor_data(data, 'data.txt')
