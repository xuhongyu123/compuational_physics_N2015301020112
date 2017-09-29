# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:28:59 2017

@author: pc
"""

def euler(t0,x0,dt,v):
    (t,x)=(t0,x0)
    while t <= 10:
        print("%f,%f" %(t,x))
        t+=dt
        x+=v*dt
euler(0,0,0.05,40)