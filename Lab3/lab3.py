#!usr/bin/env python3
'''
@author Matthew Hoeper
'''

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from math import pi
import scipy

x = np.arange(0,4*pi,0.05)
y = np.sin(x)

plt.plot(x,y)
plt.title('y = sin(x)')
plt.ylabel('y')
plt.xlabel('x')
plt.show()

### PART 3
def rand_samp(n):
	u = []
	for i in range(n):
		v = np.random.uniform(0,1,10)
		# https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.uniform.html
		u.append(sum(v))
	return u
t = rand_samp(10000)

plt.hist(t)
plt.ylabel("Number of Occurrences")
plt.xlabel("Sum of 10 random Numbers")
plt.show()


### PART 4
from msd import *

smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
state, t = smd.simulate(0.0, 1.0)

plt.plot(state)
plt.ylabel("Position (m), Velocity (m/s)")
plt.xlabel("Time (s)")
blue_patch = mpatches.Patch(color='blue', label='Position')
orange_patch = mpatches.Patch(color='orange', label='Velocity')
plt.legend(handles=[blue_patch,orange_patch])
plt.show()

### PART 5
import random
from time import time
from time import sleep
n = [1, 10, 100, 1000, 10000, 100000, 1000000]
sort_time = []
sum_time = []
for i in range(len(n)):
	a = np.random.random_sample((n[i],))
	# https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.random_sample.html#numpy.random.random_sample
	start_time = time()
	for j in a:
		new = sorted(a)
	end_time = time() - start_time
	sort_time.append(end_time)

	print("{0:.10f}".format(sort_time[i]))

	start_time = time()
	sum(a)
	end_time = time() - start_time
	sum_time.append(end_time)

	#print("{0:.10f}".format(sum_time[i]))


plt.plot(n, sum_time)
plt.ylabel("Time (s)")
plt.xlabel("Length of List")
plt.show()