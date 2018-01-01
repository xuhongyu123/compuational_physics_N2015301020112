import matplotlib.pyplot as pl
import numpy as np
import math
import random
class walker(object):
    x=0,y=0
    nonlock=1
    dire=0
    def __init__(self,x,y,nonlock):
                self.x=x
                self.y=y
                self.nonlock=nonlock
    def trappiont(self):
                if self.nonlock==1:
                        self.nonlock=0
                        return
                else:
                        print 'error'
                        return
    def movewalker(self):
                if self.dire==0:
                        self.x=self.x+0.1
                elif self.dire==1:
                        self.x=self.x-0.1
                elif self.dire==2:
                        self.y=self.y-0.1
                elif self.dire==3:
                        self.y=self.y+0.1
                else :
                        print 'error4'
                self.idir=random.randint(0,3)
		s=random.randint(1,100)
		if s<=25:
			self.dire=3
		elif s<=50:
			self.dire=2
		elif s<=75:
			self.dire=1
		else:
			self.dire=0
		co=[self.x,self.y]
		if self.x>100 or self.x<-100 or self.y>100 or self.y<-100:
			self.free=0
                return co
        def changeidir(self):
                self.idir=random.randint(0,3)
                return
if __name__=='__main__':
        sc=walker(0,0,1)
        n=0
	x=[]
	y=[]
	st=[]
	x1=[]
	x2=[]
	su=0
        while sc.nonlock==1:
                s=sc.movewalker()
		x.append(s[0])
		y.append(s[1])
		su=su+s[0]**2
		print s
		n=n+1
		x1.append(su/n)
		st.append(n)
		print n
        print n
        pl.plot(x,y,'*')
	pl.title('Random walk in two dimension')
	pl.xlabel('x')
	pl.ylabel('y')
	pl.show()