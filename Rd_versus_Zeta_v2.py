"""
Created on Mon Feb 19 15:48:12 2018

@author: Michael Persinger
"""
#This script plots the Deformation Response Factor (Rd) and the Phase Angle (phi)
# as a function of w/w_n (between 0 and 5) for damping ratios 1%, 5%, 10%, 20%, 40%

import matplotlib.pyplot as plt
import numpy as np

#Calculating t and u(t)
w_ratio = [range(0,50,500)] #Ratio: forcing frequency over natural
#                                       frequency (i.e. .01,.02,...,4.99,5.00)
zeta = [0.01, 0.05, 0.10, 0.20, 0.40] #List of 5 damping ratios
rd = []
#Plotting
plt.clf()
f, (ax1,ax2) = plt.subplots(2, sharex=True)
ax1.set_title('Problem 5 Plots')
for damping in zeta:
    for w in w_ratio:
        rd_val = (1 / ((1 - float(w)**2)**2 + (2*float(damping)*float(w)**2)**0.5)
        rd.append(rd_val)
rd_np = np.array(rd)
w_np = np.append(w_ratio)
ax1.plot(w_ratio, Rd)
ax1.set(ylabel='Deformation Response Factor')
ax1.set(xlabel='$\omega/\omega_n$') 
    
##commented out second plot due to ValueError: x and y must have same first
#   dimension, but have shapes (500L,) and (1L, 500L)
#   vvvvvvvvvvvvvvvvvvv
"""for damping in zeta:
    np.seterr(divide='ignore', invalid='ignore')
    phi = np.arctan(2*damping*w_ratio / [1 - np.power(w_ratio, 2)]) * np.size(w_ratio.size)
    ax2.plot(w_ratio, phi)
    ax2.set(ylabel='phi')
 """   
plt.grid()
plt.show()