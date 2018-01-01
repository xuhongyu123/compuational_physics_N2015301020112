# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:55:31 2018

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt
steps = np.linspace(0, 5000, 5001)
x = np.zeros(5001)
y = np.zeros(5001)
z = np.zeros(5001)
for i in range(5000):
    r = np.random.rand()
    if r<0.8:
        y[i] =y[i-1]+ 0.1
    else:
        y[i] =y[i-1]- 0.1
for i in range(5000):
    r = np.random.rand()
    if r<0.8:
        z[i] =z[i-1]+ 0.1
    else:
        z[i] =z[i-1]- 0.1
for i in range(5000):
    r = np.random.rand()
    if r<0.8:
        x[i] =x[i-1]+ 0.1
    else:
        x[i] =x[i-1]- 0.1
plt.scatter(steps, x,c='blue',label='1st')
plt.scatter(steps, y,c='green',label='2nd')
plt.scatter(steps, z,c='red',label='3rd')
plt.xlim(0,5000)
plt.grid(True)
plt.xlabel('step number')
plt.ylabel('x/m')
plt.title('Random walk in one dimension')
plt.legend()
plt.show()
