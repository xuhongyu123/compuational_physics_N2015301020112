# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:27:46 2018

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt
steps = np.linspace(0, 5000, 5001)
ave = np.zeros(5001)
x = np.zeros(5001)
x2 = np.zeros(5001)
for i in range(5000):
    for j in range(5000):
        ruler = np.random.rand()
        if ruler<=0.5:
            x[j] = x[j] + 0.5
        else:
            x[j] = x[j] - 0.5
        x2[j] = x[j]**2
    average = sum(x2)/5000
    ave[i+1] = average
plt.scatter(steps, ave,s=1)
plt.xlim(0,5000)
plt.ylim(0,1500)
plt.grid(True)
plt.xlabel('step number(= time)')
plt.ylabel('<x^2>')
plt.title('<x^2>')
plt.show()