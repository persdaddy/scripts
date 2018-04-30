# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 20:52:12 2018

@author: Michael
"""
#%% Import packages
import numpy as np
import matplotlib.pyplot as plt

#%% SDOF Constants and Parameters of System
k = 24.88 # SDOF stiffness in kN/m
m = 31.55 # SDOF mass in kg
#zeta = 0.05 # SDOF damping ratio
wn = 0.89 # SDOF Natural Frequency in rad/s
#wn = (np.sqrt(k/m)) # SDOF Natural Frequency
Tn = 5.58 #SDOF Natural Period in sec
#Tn = (2* np.pi / wn) # SDOF Natural Period in sec
c = (zeta*wn/(2*k)) # SDOF damping constant
beta = 0.166666667
gamma = 0.5

#%% Time and force vectors
tfinal = 1.7 # Simulation time
dt = 0.001 # Delta time
t = np.array((0., 0.1, 0.12, 0.16, 0.2, 0.3, 0.4, 1., 2.)) # Time vector
p = np.array((0., 0., 66., 29., 23.5, 12., 4., 0., 0.)) # Force vector

t1 = np.arange(0,30,dt)
pinterp = np.interp(t1,t,p)


#%% Vectors displacement , velocity and acceleration
u = np.zeros ( t1.shape )
udot = np.zeros ( t1.shape )
uddot = np.zeros ( t1.shape )

#%% Setting initial conditions for displacement and velocity
u[0] = 0.
udot[0] = 0.
uddot[0] = 0.

#%% Initial Calculations
try:
    a1 = 1/(beta*t**2)*m + gamma/(beta*t)*c
    a2 = 1/(beta*t)*m + (gamma/beta -1)*c
    a3 = (1/(2*beta)-1)*m + t*(gamma/(2*beta)-1)*c
    khat = k + a1
except ZeroDivisionError:
    a1 = 9999999
    a2 = 9999999
    a3 = 9999999

#%% Main loop for Average Acceleration method
for i in range ( len ( t ) -1 ):
    pihat = p[i+1] + a1*u[i] + a2*udot[i] + a3*uddot[i]
    u[i+1] = pihat/khat
    udot[i+1] = gamma/(beta*t)*(u[i+1] - u[i]) + (1-gamma/beta)*udot[i] + t*(1-gamma/(2*beta))*uddot[i]
    uddot[i+1] = 1/(beta*t**2)*(u[i+1] - u[i]) - 1/(beta*t)*udot[i] - (1/(2*beta) - 1)*uddot[i]
print dt/Tn

#%% Plotting
plt.clf ()
plt.plot (t1, u )
plt.title('Linear Acceleration Method (0.001s timestep)')
plt.xlabel ('$t$ (s)')
plt.ylabel ('$u$ (in)')
plt.grid ()