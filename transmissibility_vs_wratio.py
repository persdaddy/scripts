# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:21:13 2018

@author: Michael
"""
#This script plots the transmissibility (TR)
# as a function of w/w_n (between 0 and 20) for damping ratios 1%, 5%, 10%, 20%, 40%

import matplotlib.pyplot as plt
import numpy as np

#Calculating t and u(t)
w_ratio = np.linspace(0.0,20.0,20000) #Ratio: forcing frequency over natural
#                                       frequency (i.e. .1,.2,...,19.9,20.00)
zeta = np.array([0.01, 0.05, 0.10, 0.20, 0.40]) #List of 5 damping ratios
#print len(zeta)
#print len(w_ratio)

x = []



#Plotting
plt.clf()
plt.title('Problem 5 Plots')

for damping in zeta:
    trans = (1 + (2*zeta*ratio)**2 /((1 - (ratio**2))**2 + (2*damping*ratio)**2))**0.5
    np.append(y, trans)  
    plt.plot(w_ratio, y)
    print len(y)
plt.xlabel('$\omega/\omega_n$') 
plt.ylabel('Transmissibility')
plt.grid()
plt.show()