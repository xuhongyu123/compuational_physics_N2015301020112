# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:28:59 2017

@author: pc
"""
import matplotlib.pyplot as plt
t=0
x=0
list_time=[t]
list_position=[x]
def euler(t,x,dt,v):    
    while t <= 10:
        print("%f,%f" %(t,x))
        t+=dt
        x+=v*dt
        list_time.append(t)
        list_position.append(x)
euler(0,0,0.05,40)
plt.plot(list_time,list_position)
plt.ylabel('position(m)')
plt.xlabel('time(s)')
plt.title('x-t')
plt.ylim(0,400)
plt.xlim(0,10)
plt.show()