# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 09:49:11 2018

@author: Michael
"""

#%% Import packages
import numpy as np
import matplotlib.pyplot as plt

#%% SDOF Constants and Parameters of System
k = 10. # SDOF stiffness in kips/in
m = 0.2533 # SDOF mass in kip-sec^2/in
zeta = 0.05 # SDOF damping ratio
wn = np.sqrt(k/m) # SDOF Natural Frequency
Tn = 2* np.pi / wn # SDOF Natural Period = 1
c = zeta*wn/(2*k) # SDOF damping constant

#%% Time and force vectors
tfinal = 1.6 # Simulation time
dt = 0.05 # Delta time
t = np.array ( np.arange(0, tfinal, dt)) # Time vector
p = np.array ( 10*np.sin(np.pi*t/0.6) ) # Force vector
p[t>=0.6] = 0

#%% Vectors displacement , velocity and acceleration
u = np.zeros ( t.shape )
udot = np.zeros ( t.shape )
uddot = np.zeros ( t.shape )

#%% Setting initial conditions for displacement and velocity
u[0] = 0.
udot[0] = 0.

#%% Initial parameters for central difference method
uddot[0] = ( p[0] - c * udot[0] -k * u[0])/ m
u[-1] = u[0] - dt * udot[0] + ( dt )**2 * uddot[0] / 2
khat = m /( dt **2) + c /(2* dt )
a = m /( dt **2) - c /(2* dt )
b = k - (2* m )/( dt **2)

#%% Main loop for central difference method
for i in range ( len ( t ) - 1):
    pihat = p[i] - a * u[i -1] - b * u[i]
    u[i +1] = pihat / khat

#%% Plotting
plt.clf ()
plt.plot (t, u)
plt.title('Central Difference Method (0.05s timestep)')
plt.xlabel ('$t$ (s)')
plt.ylabel ('$u$ (in)')
plt.grid ()
