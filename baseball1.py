# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:28:59 2017

@author: pc
"""
import matplotlib.pyplot as plt
import math
vx0=31.3
vy0=0
list_x=[]
list_y=[]
def euler(x0,y0,dt):
     x,y=x0,y0
     vx,vy=vx0,vy0
     while x <= 18.3:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))
        y+=vy*dt
        vy+=(0.00041*vx*200/3*math.pi-9.8)*dt
        list_x.append(x)
        list_y.append(y)
euler(0,1.98,0.05)

list_a=[]
list_b=[]
def euler(x0,y0,dt):    
     x,y=x0,y0
     vx,vy=vx0,vy0
     while x <= 18.3:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))
        y+=vy*dt
        vy+=-9.8*dt
        list_a.append(x)
        list_b.append(y)
euler(0,1.98,0.05)

list_c=[]
list_d=[]
def euler(x0,y0,dt):
     x,y=x0,y0
     vx,vy=vx0,vy0
     while x <= 18.3:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))
        y+=vy*dt
        vy+=(-9.8-0.00041*vx*200/3*math.pi)*dt
        list_c.append(x)
        list_d.append(y)
euler(0,1.98,0.05)
plt.plot(list_x,list_y, label='backspin')
plt.plot(list_a,list_b, label='no spin')
plt.plot(list_c,list_d, label='overhand')
plt.ylabel('height(m)')
plt.xlabel('position(m)')
plt.title('x-y')
plt.ylim(0,2)
plt.xlim(0,18.3)
plt.legend()
plt.show()
