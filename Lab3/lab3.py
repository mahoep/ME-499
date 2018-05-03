#!usr/bin/env python3
'''
@author Matthew Hoeper
'''

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from math import pi

from rand_samp import *
from msd import *
from rand_sort import *
from rand_sum import *

### PART 2
x = np.arange(0, 4 * pi, 0.05)
y = np.sin(x)

plt.plot(x, y)
plt.title('y = sin(x)')
plt.ylabel('y')
plt.xlabel('x')
plt.show()

### PART 3
t = rand_samp(10000)
plt.hist(t)
plt.ylabel("Number of Occurrences")
plt.xlabel("Sum of 10 random Numbers")
plt.title("Distribution of 10,000 Random Numbers")
plt.show()


### PART 4
smd = MassSpringDamper(m=10.0, k=10.0, c=1.5)
state, t = smd.simulate(1, 10)
plt.plot(t, state)
plt.ylabel("Position (m), Velocity (m/s)")
plt.xlabel("Time (s)")
blue_patch = mpatches.Patch(color='blue', label='Position')
orange_patch = mpatches.Patch(color='orange', label='Velocity')
plt.legend(handles=[blue_patch,orange_patch])
plt.title("Damped Mass Spring System, m=10, k=10,c=1.5")
plt.show()

### PART 5
n = [1, 10, 100, 1000, 10000, 100000, 1000000]

sort_time = rand_sort(n)
plt.semilogx(n, sort_time)

sum_time = rand_sum(n)
plt.semilogx(n, sum_time)
plt.ylabel("Time (ms)")
plt.xlabel("Length of List")
plt.title("Operation Times")
blue_patch = mpatches.Patch(color='blue', label='Sorting O(nlogn)')
orange_patch = mpatches.Patch(color='orange', label='Summing O(n)')
plt.legend(handles=[blue_patch,orange_patch])
plt.show()
