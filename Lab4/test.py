#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''
import numpy as np
from complex import Complex


Data = np.random.random((100, 100, 1000, 2))
result = np.empty(Data.shape[:-1], dtype=complex)
print(Data[0,0,0,0], Data[0,0,0,1], result[0,0,0])


a = Complex(1.0, 2.3)  # 1 + 2.3i
b = Complex(2)  # 2 + 0i
c = Complex()  # 0 + 0i

a = Complex(1, 2)
b = Complex(1, -2)
print(a)
print(b)

c = Complex(1.2, 3.4)
print(c.im)
print(c.re)

a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)  # (4 + 6i)
print(a + 1)  # (2 + 2i)
print(1 + a)     # (2 + 2i)

print(a - b)  
print(a - 1)
print(1 - a)