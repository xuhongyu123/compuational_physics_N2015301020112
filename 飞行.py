# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:28:59 2017

@author: pc
"""
import matplotlib.pyplot as plt
import math
v0=700
list_x=[]
list_y=[]
def euler(x0,y0,dt):    
     vx0=math.cos(math.pi/4)*v0
     vy0=math.sin(math.pi/4)*v0
     x,y=x0,y0
     vx,vy=vx0,vy0
     while y >= 0:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        y+=vy*dt
        vy+=-9.8*dt-0.00004*vy**2*dt/math.sin(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        list_x.append(x)
        list_y.append(y)
euler(0,0,0.05)

list_a=[]
list_b=[]
def euler(x0,y0,dt):    
     vx0=math.cos(43.6*math.pi/180)*v0
     vy0=math.sin(43.6*math.pi/180)*v0
     x,y=x0,y0
     vx,vy=vx0,vy0
     while y >= 0:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        y+=vy*dt
        vy+=-9.8*dt-0.00004*vy**2*dt/math.sin(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        list_a.append(x)
        list_b.append(y)
euler(0,0,0.05)

list_c=[]
list_d=[]
def euler(x0,y0,dt):    
     vx0=math.cos(40*math.pi/180)*v0
     vy0=math.sin(40*math.pi/180)*v0
     x,y=x0,y0
     vx,vy=vx0,vy0
     while y >= 0:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        y+=vy*dt
        vy+=-9.8*dt-0.00004*vy**2*dt/math.sin(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        list_c.append(x)
        list_d.append(y)
euler(0,0,0.05)

list_e=[]
list_f=[]
def euler(x0,y0,dt):    
     vx0=math.cos(35*math.pi/180)*v0
     vy0=math.sin(35*math.pi/180)*v0
     x,y=x0,y0
     vx,vy=vx0,vy0
     while y >= 0:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        y+=vy*dt
        vy+=-9.8*dt-0.00004*vy**2*dt/math.sin(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        list_e.append(x)
        list_f.append(y)
euler(0,0,0.05)
list_q=[]
list_w=[]
def euler(x0,y0,dt):    
     vx0=math.cos(30*math.pi/180)*v0
     vy0=math.sin(30*math.pi/180)*v0
     x,y=x0,y0
     vx,vy=vx0,vy0
     while y >= 0:
        x+=vx*dt
        vx+=-0.00004*vx**2*dt/math.cos(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        y+=vy*dt
        vy+=-9.8*dt-0.00004*vy**2*dt/math.sin(math.atan(vy/vx))*(1-0.0065*y/300)**2.5
        list_q.append(x)
        list_w.append(y)
euler(0,0,0.05)
plt.plot(list_x,list_y, label='45')
plt.plot(list_a,list_b, label='43.6')
plt.plot(list_c,list_d, label='40')
plt.plot(list_e,list_f, label='35')
plt.plot(list_q,list_w, label='30')
plt.ylabel('height(m)')
plt.xlabel('position(m)')
plt.title('x-y')
plt.ylim(0,8000)
plt.xlim(0,25000)
plt.legend()
plt.show()
plt.plot(list_x,list_y, label='45')
plt.plot(list_a,list_b, label='43.6')
plt.plot(list_c,list_d, label='40')
plt.plot(list_e,list_f, label='35')
plt.plot(list_q,list_w, label='30')
plt.ylabel('height(m)')
plt.xlabel('position(m)')
plt.title('x-y')
plt.ylim(0,400)
plt.xlim(22500,24550)
plt.legend()
plt.show()