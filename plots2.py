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
sp = plt.subplot(221)
plt.plot(x, np.sin(x))
plt.title(r'$sin(x)$')
plt.grid(True)