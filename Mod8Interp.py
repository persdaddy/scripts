# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 11:54:01 2018

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

#%% Time and force vectors
tfinal = 1.7 # Simulation time
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


#%% Initial Calculations
expt = (np.exp(-1*zeta*wn*dt))
wd = (wn*np.sqrt(1-zeta**2))
sin = (np.sin(wd*dt))
cos = (np.cos(wd*dt))

A = expt*(zeta/np.sqrt(1-zeta**2)*sin + cos ) 
B = expt*(1/wd*sin)
C = 1/k *(2*zeta/(wn*dt) + expt*(((1-2*zeta**2)/(wd*dt) - zeta/(np.sqrt(1-zeta**2) ))*sin - (1+2*zeta/(wn*dt)) *cos))
D = 1/k *(1-2*zeta/(wn*dt) + expt*((2*zeta**2 - 1)/(wd*dt)*sin + 2*zeta/(wn*dt)*cos))
Ap = -1*expt*(wn*sin/(np.sqrt(1-zeta**2)))
Bp = expt*(cos - zeta/(np.sqrt(1-zeta**2))*sin)
Cp = 1/k *(-1/dt + expt*((wn/np.sqrt(1-zeta**2)+zeta/(dt*np.sqrt(1-zeta**2)))*sin + 1/dt*cos))
Dp = 1/(k*dt)*(1-expt*(zeta/np.sqrt(1-zeta**2)*sin + cos))

#%% Main loop for piecewise interpolation method

"""output1 = open('C:/Users/Michael/Documents/JHU - Structural Dynamics/Mod8LinIntOutput.csv','w')
header1 = [' ',' ',' ','A',' ','ui',' ','B',' ','ui',' ','C',' ','pi',' ','D',' ','pi+1\n']
headerline = ','.join(header1)
output1.write(headerline)

output2 = open('C:/Users/Michael/Documents/JHU - Structural Dynamics/Mod8LinIntOutput2.csv','w')
header2 = [' ',' ',' ','Ap',' ','ui',' ','Bp',' ','ui',' ','Cp',' ','pi',' ','Dp',' ','pi+1\n']
headerline2 = ','.join(header2)
output2.write(headerline2)"""
for i in range ( len ( t ) - 1 ):
    u[i+1] = A*u[i] + B*udot[i] + C*p[i] + D*p[i+1]
    udot[i+1] = Ap*u[i] + Bp*udot[i] + Cp*p[i] + Dp*p[i+1]
    
"""    check = ['Timestep=',str(dt),' -> u[i+1] = ',str(A),'*',str(u[i]),' + ',str(B),'*',str(udot[i]),' + ',str(C),'*',str(p[i]),' + ',str(D),'*',str(p[i+1]),' = ', str(u[i+1])]
    line = ','.join(check)
    output1.write(line + '\n')
    check2 = ['Timestep=',str(dt),' -> udot[i+1] = ',str(Ap),'*',str(udot[i]),' + ',str(Bp),'*',str(udot[i]),' + ',str(Cp),'*',str(p[i]),' + ',str(Dp),'*',str(p[i+1]),' = ', str(udot[i+1])]
    line = ','.join(check2)
    output2.write(line + '\n')
output1.close()
output2.close()"""
    #print 'ti =', t[i], "D'pi+1 =", Dp*p[i+1]
#'pi =', p[i], 'Cpi =', C*p[i], 'Dpi+1 =', D*p[i+1], 'Budoti =', B*udot[i],
#'udoti =', udot[i],'Aui =', A*u[i], "C'pi =", Cp*p[i],
#for i in range ( len ( t ) - 1):
    #pihat = p[i] - a * u[i -1] - b * u[i]
    #u[i +1] = pihat / khat

#%% Plotting
plt.clf ()
plt.plot (t, u )
plt.title('Piecewise Interpolation Method')
plt.xlabel ('$t$ (s)')
plt.ylabel ('$u$ (in)')
plt.grid ()
