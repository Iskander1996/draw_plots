#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:41:55 2021

@author: iskander
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10.0, 10.01, 0.01)
t = np.arange(-10, 11, 1)

#subplot 1
sp = plt.subplot(2,2,1)
plt.plot(x, np.sin(x))
plt.title(r'$sin(x)$')
plt.grid(True)

#subplot 2

sp = plt.subplot(2,2,2)
plt.plot(x, np.cos(x), 'g')
plt.axis('equal')
plt.grid(True)
plt.title(r'$cos(x)$')

#subplot 3
sp = plt.subplot(2, 2, 3)
plt.plot(x, x**2, t, t**2, 'ro')
plt.title(r'$x^2$')

#subplot 4
sp = plt.subplot(2, 2 ,4)
plt.plot(x, x)
np.spines['left'].set_position('center')
np.spines['bottom'].set_position('center')
plt.grid(True)
plt.title(r'$x$')
plt.show()
