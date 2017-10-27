# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:28:59 2017

@author: pc
"""
import matplotlib.pyplot as plt
import math
list_x=[]
list_y=[]
list_t=[]
list_E=[]
def euler(x0,y0,F,E0,t0,dt):
     x,y,t,E=x0,y0,t0,E0
     while t <= 80:
         y += -math.sin(x)*dt-0.5*y*dt+F*math.sin(2/3*t)*dt
         x += y*dt
         t += dt
         E += 0.5*9.8*9.8*(y*y+x*x)*dt*dt
         while x <= -math.pi:
             x += 2*math.pi
         while x >= math.pi: 
             x += -2*math.pi
         list_x.append(x)
         list_y.append(y)
         list_t.append(t)
         list_E.append(E)
euler(0.2,0,0.1,1.92,0,0.04)
list_a=[]
list_b=[]
list_c=[]
list_F=[]
def euler(x0,y0,F,E0,t0,dt):
     x,y,t,E=x0,y0,t0,E0
     while t <= 80:
         y += -math.sin(x)*dt-0.5*y*dt+F*math.sin(2/3*t)*dt
         x += y*dt
         t += dt
         E += 0.5*9.8*9.8*(y*y+x*x)*dt*dt
         while x <= -math.pi:
             x += 2*math.pi
         while x >= math.pi: 
             x += -2*math.pi
         list_a.append(x)
         list_b.append(y)
         list_c.append(t)
         list_F.append(E)
euler(0.2,0,0.5,1.92,0,0.04)
list_d=[]
list_e=[]
list_f=[]
list_G=[]
def euler(x0,y0,F,E0,t0,dt):
     x,y,t,E=x0,y0,t0,E0
     while t <= 80:
         y += -math.sin(x)*dt-0.5*y*dt+F*math.sin(2/3*t)*dt
         x += y*dt
         t += dt
         E += 0.5*9.8*9.8*(y*y+x*x)*dt*dt
         while x <= -math.pi:
             x += 2*math.pi
         while x >= math.pi: 
             x += -2*math.pi
         list_d.append(x)
         list_e.append(y)
         list_f.append(t)
         list_G.append(E)
euler(0.2,0,0.99,1.92,0,0.04)
plt.plot(list_t,list_x, label='Fd=0.1')
plt.plot(list_c,list_a, label='Fd=0.5')
plt.plot(list_f,list_d, label='Fd=0.99')
plt.ylabel('Θ(radians)')
plt.xlabel('time(s)')
plt.title('Θ versus time')
plt.ylim(-4,5)
plt.xlim(0,80)
plt.legend()
plt.show()
plt.plot(list_x,list_y, label='Fd=0.5')
plt.plot(list_a,list_b, label='Fd=0.5')
plt.plot(list_d,list_e, label='Fd=0.99')
plt.xlabel('Θ(radians)')
plt.ylabel('ω(radians/s)')
plt.title('ω versus Θ')
plt.legend()
plt.show()
plt.plot(list_t,list_E, label='Fd=0.1')
plt.plot(list_c,list_F, label='Fd=0.5')
plt.plot(list_f,list_G, label='Fd=0.99')
plt.ylabel('energy(J)')
plt.xlabel('time(s)')
plt.title('Energy versus time')
plt.ylim(1.9,50)
plt.xlim(0,80)
plt.legend()
plt.show()