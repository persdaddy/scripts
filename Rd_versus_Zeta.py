"""
Created on Mon Feb 19 15:48:12 2018

@author: Michael Persinger
"""
import matplotlib.pyplot as plt
import numpy as np

#Calculating t and u(t)
w_ratio = np.array(range(500)) * 0.01 #Time vector
zeta = np.array([0.01, 0.05, 0.10, 0.20, 0.40]) #List of damping ratios


#Plotting
plt.clf()

#Create two subplots for sharing x axis
f, axarr = plt.subplots(nrows=2, sharex=True)
f.suptitle('Problem 5 Plots') 
for damping in zeta:
    Rd = (1 / np.sqrt(np.power(1 - w_ratio, 2) + np.power(2*damping*w_ratio, 2)))
    phi = np.arctan(2*damping*w_ratio / [1 - np.power(w_ratio,2)])
        
    axarr[0].plot(w_ratio, Rd)
    axarr[0].set(ylabel='Deformation Response Factor')
    
    axarr[1].plot(w_ratio, phi)
    axarr[1].set(xlabel='$\omega/\omega_n$', ylabel='phi') #u'\u03C6')
    
plt.grid()
plt.show()