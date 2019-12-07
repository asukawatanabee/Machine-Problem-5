#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:38:38 2019

@author: asukawatanabe
"""
from matplotlib import pyplot as plt
import math
def x_of_n(n):
    return math.sin((3*math.pi*n) / 100)

def y_of_n(n):
    if n==0:
        return -1.5*x_of_n(n) + 2*x_of_n(n+1) - 0.5*x_of_n(n+2)
    elif n>0 and n<=198:
        return 0.5*x_of_n(n+1) - 0.5*x_of_n(n-1)
    elif n==199:
        return 1.5*x_of_n(n) - 2*x_of_n(n-1) + 0.5*x_of_n(n-2)

n_val = list(range(200))
x_val = [x_of_n(n) for n in n_val]
y_val = [y_of_n(n) for n in n_val]

plt.plot(n_val, x_val, label = 'Value of x(n)')
plt.plot(n_val, y_val, label = 'Value of y(n)')
plt.legend()
plt.show()