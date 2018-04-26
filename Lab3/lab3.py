#!usr/bin/env python3
'''
@author Matthew Hoeper
'''

import matplotlib.pyplot as plt
import numpy as np
import math as mth
import scipy

x = np.arange(0,4*mth.pi,0.05)
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

