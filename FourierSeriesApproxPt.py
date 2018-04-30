# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:24:59 2018

@author: Michael
"""

# Importing packages
import numpy as np
import matplotlib.pyplot as plt

# Constants
To = 3
wo = 2* np.pi / To

# Time vector
dt = 0.01
t = np.array ( range ( int (3 / dt )+1)) * dt

js = np.array ( range (1 ,300)) # J to use in the series
p = np.zeros ( t.shape )
for j in js :
    if ( j % 3 > 0): # Do not use the j multiple of 3
        p += 3000 / ( np.pi * j ) * np.sin ( j * wo * t )

plt.clf ()
plt.plot (t , p )
plt.xlabel ('Time (s)')
plt.ylabel ('Force (N)')
plt.axis ([0 , 3 , -1500 , 1500])
plt.grid ()