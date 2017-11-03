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
def euler(x0,y0,F,t0,dt):
     x,p,y,q,t,z=x0,x0,y0,y0,t0,9.424777
     for i in range(1,1000000):
         y += -math.sin(x)*dt-0.5*y*dt+F*math.sin(2/3*t)*dt
         x += y*dt
         while x <= -math.pi:
             x += 2*math.pi
         while x >= math.pi: 
             x += -2*math.pi
         while  -0.01<t-z<0.01:
             p,q=x,y
             list_x.append(p)
             list_y.append(q)
             list_t.append(z)
             z += 9.424777
         t += dt
euler(0.2,0,1.4,0,0.01)
list_a=[]
list_b=[]
list_c=[]
def euler(x0,y0,F,t0,dt):
     x,p,y,q,t,z=x0,x0,y0,y0,t0,9.424777
     for i in range(1,1000000):
         y += -math.sin(x)*dt-0.5*y*dt+F*math.sin(2/3*t)*dt
         x += y*dt
         while x <= -math.pi:
             x += 2*math.pi
         while x >= math.pi: 
             x += -2*math.pi
         while  -0.01<t-z<0.01:
             p,q=x,y
             list_a.append(p)
             list_b.append(q)
             list_c.append(z)
             z += 9.424777
         t += dt
euler(0.2,0,1.44,0,0.01)
list_d=[]
list_e=[]
list_f=[]
def euler(x0,y0,F,t0,dt):
     x,p,y,q,t,z=x0,x0,y0,y0,t0,9.424777
     for i in range(1,1000000):
         y += -math.sin(x)*dt-0.5*y*dt+F*math.sin(2/3*t)*dt
         x += y*dt
         while x <= -math.pi:
             x += 2*math.pi
         while x >= math.pi: 
             x += -2*math.pi
         while  -0.01<t-z<0.01:
             p,q=x,y
             list_d.append(p)
             list_e.append(q)
             list_f.append(z)
             z += 9.424777
         t += dt
euler(0.2,0,1.465,0,0.01)
plt.plot(list_x,list_y,'.', label='Fd=1.4')
plt.xlabel('Θ(radians)')
plt.ylabel('ω(radians/s)')
plt.title('ω versus Θ')
plt.legend()
plt.show()
plt.plot(list_a,list_b,'.', label='Fd=1.44')
plt.xlabel('Θ(radians)')
plt.ylabel('ω(radians/s)')
plt.title('ω versus Θ')
plt.legend()
plt.show()
plt.plot(list_d,list_e,'.', label='Fd=1.465')
plt.xlabel('Θ(radians)')
plt.ylabel('ω(radians/s)')
plt.title('ω versus Θ')
plt.legend()
plt.show()