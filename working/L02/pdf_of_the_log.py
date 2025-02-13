# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 15:52:47 2024

@author: ISAFA
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.uniform(0.1, 10, N) #creation of a uniform distribution

#histogram of it
fig = plt.figure(figsize=(8,6)) 
ax = fig.gca()
ax.hist(x, bins=100, density = True) 
#ax.legend()
ax.set_title('Uniform distribution histogram')

#log10(x)
y= np.log10(x)

#histogram of log10(x)
fig1 = plt.figure(figsize=(8,6)) 
ax1 = fig1.gca()
ax1.hist(y, bins=100, density = True)
#ax.legend()
ax1.set_title('Log10 histogram')

#equation to derive the pdf of f(x): p(y)=abs(dx/dy)p(x)= abs(dy/dx)^-1p(x)

p_x=1/(10-0.1)                     #pdf of uniform distribution that is 1/(b-a)
p_y= p_x/(abs(1/(np.log(10)*x)))   #pdf of the log10(x)
                                   #also: p_y= p_x*abs((10**y)*np.log(10))
#plot of pdfs
p_x = np.ones(N)*p_x             
ax.plot(x, p_x, color='red')
ax1.scatter(y, p_y, color='red', s= 3)

#mean and median of log10(x) and y, the median are the same
log_mean_x = np.log10(np.mean(x))
mean_y = np.mean(y)
print('log(mean_x) =', log_mean_x)
print('mean_y =', mean_y)
ax1.vlines(log_mean_x, 0, 3, color='green')
ax1.vlines(mean_y, 0, 3, color='forestgreen')

log_median_x = np.log10(np.median(x))
median_y = np.median(y)
print('log(median_x) =', log_median_x)
print('median_y =', median_y)
ax1.vlines(log_median_x, 0, 3, color='mediumorchid')
ax1.vlines(median_y, 0, 3, color='orchid')