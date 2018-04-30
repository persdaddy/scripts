# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:25:05 2018

@author: Michael
"""
import numpy as np
from scipy import linalg
#E=1
#I=1
#h=1
#m=1
#k = 24*E*I/h**3
k=24

km = k*np.array([[2.,-1.],[-1.,1.]])
mm = np.array([[1.,0],[0,0.5]])

w,v = linalg.eigh(km,mm)
w1,w2 = np.sqrt(w)
print 'Frequencies: w1 = ', w1, 'w2 = ',w2
print v, '\n'

#spectral = np.array([[w1, 0],[0,w2]])
#spectral = np.diag(w)
#print km*v,'\n'
#print mm*v*spectral**2