# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 22:00:54 2018

@author: Michael
"""

#%% Import packages
import numpy as np
import matplotlib.pyplot as plt

#%% SDOF Constants and Parameters of System
k = 10. # SDOF stiffness in kips/in
m = 0.2533 # SDOF mass in kip-sec^2/in
zeta = 0.05 # SDOF damping ratio
wn = (np.sqrt(k/m)) # SDOF Natural Frequency
Tn = (2* np.pi / wn) # SDOF Natural Period = 1
c = (zeta*wn/(2*k)) # SDOF damping constant
beta = 0.25
gamma = 0.5

#%% Time and force vectors
tfinal = 1.6 # Simulation time
dt = 0.1 # Delta time
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
uddot[0] = 0.

#%% Initial Calculations
a1 = 1/(beta*dt**2)*m + gamma/(beta*dt)*c
a2 = 1/(beta*dt)*m + (gamma/beta -1)*c
a3 = (1/(2*beta)-1)*m + dt*(gamma/(2*beta)-1)*c
khat = k + a1

#%% Main loop for Average Acceleration method
for i in range ( len ( t ) -1 ):
    pihat = p[i+1] + a1*u[i] + a2*udot[i] + a3*uddot[i]
    u[i+1] = pihat/khat
    udot[i+1] = gamma/(beta*dt)*(u[i+1] - u[i]) + (1-gamma/beta)*udot[i] + dt*(1-gamma/(2*beta))*uddot[i]
    uddot[i+1] = 1/(beta*dt**2)*(u[i+1] - u[i]) - 1/(beta*dt)*udot[i] - (1/(2*beta) - 1)*uddot[i]
    

#%% Plotting
plt.clf ()
plt.plot (t, u )
plt.title('Average Acceleration Method')
plt.xlabel ('$t$ (s)')
plt.ylabel ('$u$ (in)')
plt.grid ()
