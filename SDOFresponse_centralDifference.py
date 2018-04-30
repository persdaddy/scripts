"""
Created on Mon Feb 19 20:04:49 2018

@author: Michael
"""

"""
2 Python script to calculate the response of a SDOF
3 using the central difference method
4 """
#%% Importing packages
import numpy as np
import matplotlib . pyplot as plt

#%% SDOF Constants
k = 1.0e4 # SDOF stiffness
m = 100. # SDOF mass
c = 0. # SDOF damping constant

#%% Time and force vectors
tfinal = 3. # Simulation time
dt = np.pi /1000. # Delta time
t = np.array ( range ( int ( tfinal / dt )+1)) * dt # Time vector
p = np.zeros ( t.shape ) # Force vector

#%% Vectors displacement , velocity and acceleration
u = np.zeros ( t.shape )
udot = np.zeros ( t.shape )
uddot = np.zeros ( t.shape )

#%% Setting initial conditions for displacement and velocity
u [0] = 0.1
udot [0] = 0.2

#%% Parameters of the structure
wn = np . sqrt ( k / m )
Tn = 2* np . pi / wn

#%% Initial parameters for central difference method
uddot [0] = ( p [0] - c * udot [0] -k * u [0])/ m
u [ -1] = u [0] - dt * udot [0] + ( dt )**2 * uddot [0] / 2
khat = m /( dt **2) + c /(2* dt )
a = m /( dt **2) - c /(2* dt )
b = k - (2* m )/( dt **2)

#%% Main loop for central difference method
for i in range ( len ( t ) - 1):
    pihat = p [ i ] - a * u [i -1] - b * u [ i ]
    u [ i +1] = pihat / khat

#%% Plotting
plt . clf ()
plt . plot (t , u )
plt . xlabel ('$t$ (s)')
plt . ylabel ('$u$ (m)')
plt . grid ()
