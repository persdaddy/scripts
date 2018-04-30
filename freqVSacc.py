"""
Created on Sun Feb 25 14:41:49 2018

@author: Michael
"""
# Import Packages
import matplotlib.pylab as plt #Package for plotting
import numpy as np 
from scipy.optimize import curve_fit

# Curve Fitting
freq = np.array([1.337, 1.378, 1.4, 1.417, 1.438, 1.453, 1.462, 1.477, 1.487, 1.493, 1.497, 1.5, 1.513, 1.52, 1.53, 1.54, 1.55, 1.567, 1.605, 1.628, 1.658])
acc = np.array([.68, .90, 1.15, 1.50, 2.2, 3.05, 4.00, 7.00, 8.60, 8.15, 7.60, 7.1, 5.4, 4.7, 3.8, 3.4, 3.1, 2.6, 1.95, 1.7, 1.5])

def func(x, a, b, c, d):
    return a * np.power(x,3) + b * np.power(x,2) + c * x + d


xdata = np.linspace(1.3, 1.7, 40)
ydata = func(xdata, 1,1,1,1) * np.size(xdata.size)

popt, pcov = curve_fit(func, freq, acc)
print popt
print pcov

# Plotting
plt.clf() # Clearing any previous plots
plt.plot(freq, func(freq, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f d = %f' % tuple(popt))
plt.plot(freq, acc)
plt.xlabel('Excitation Frequency')
plt.ylabel('Acceleration (e-3 g)')
plt.grid()