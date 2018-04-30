# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:10:02 2018

@author: Michael
"""

# Import Packages
import matplotlib.pylab as plt #Package for plotting
import numpy as np 

# Calculating t and u(t)
t = np.array(range(200)) ∗ 0.01 # Time vector
u = 0.1 ∗ np.cos(10∗ t) + 0.02 ∗ np.sin(10∗ t )

# Plotting
plt.clf() # Clearing any previous plots
plt.plot(t, u)
plt.xlabel('t(s)')
plt.ylabel('u(t)(m)')
plt.grid()s