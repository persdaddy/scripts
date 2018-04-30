# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 13:49:25 2018

@author: Michael
"""

import numpy as np 
from numpy.linalg import inv
import matplotlib.pyplot as plt
from numpy import pi

# variables
m = 2.0
k = 2.0
c = 0.0   # critical damping = 2 * SQRT(m*k) = 4.0

F0 = 1.0
delta_t = 0.001
omega = 1.0
time = np.arange(0.0, 15.0, delta_t)
Tn = 2*pi*np.sqrt(m/k)

# initial state
y = np.array([0,0])   # [velocity, displacement]

A = np.array([[m,0],[0,1]])
B = np.array([[c,k],[-1,0]])
F = np.array([0.0,0.0])

Y = []
force = []
t1 = 5.0
t2 = 10.0
t3 = 15.0
td = 15.0

# time-stepping solution
for t in time:
	if t <= 5:
		F[0] = F0/k * (t/td - Tn/(2*pi*td)*np.sin(2*pi*t/Tn))
	elif t>5 and t<=10:
		F[0] = F0
	else:
		F[0] = F0 - t/t3

	y = y + delta_t * inv(A).dot( F - B.dot(y) )
	Y.append(y[1])
	force.append(F[0])

	KE = 0.5 * m * y[0]**2
	PE = 0.5 * k * y[1]**2

	if t % 1 <= 0.01:
		print 'Total Energy:', KE+PE


# plot the result
t = [i for i in time]

plt.plot(t,Y)
plt.plot(t,force)
plt.grid(True)
plt.legend(['Displacement', 'Force'], loc='lower right' )

plt.show()

print 'Critical Damping:', np.sqrt( (-c**2 + 4*m*k) / (2.0 * m) )
print 'Natural Frequency:', np.sqrt(k/m)