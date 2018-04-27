#!usr/bin/env python3
'''
@author Matthew Hoeper
'''

import matplotlib.pyplot as plt
import numpy as np
from math import pi
import scipy

x = np.arange(0,4*pi,0.05)
y = np.sin(x)

#plt.plot(x,y)
#plt.title('y = sin(x)')
#plt.ylabel('y')
#plt.xlabel('x')
#plt.show()

### PART 3
def rand_samp(n):
	u = []
	for i in range(n):
		v = np.random.uniform(0,1,10)
		u.append(sum(v))
	return u
t = rand_samp(10000)

plt.hist(t)
plt.ylabel("Number of Occurences")
plt.xlabel("Sum of 10 random Numbers")
plt.show()


### PART 4
from msd import *

smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
state, t = smd.simulate(0.0, 1.0)

# for s in state:
#   print(s[0)]
import matplotlib.pyplot as plt

plt.plot(state)
plt.show()


### PART 5