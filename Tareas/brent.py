# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:11:17 2021

@author: andre
"""

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def fun(x):
    return  (x**3) -(2*x**2) + (4/3)*x - (8/27)

(r1,it) = optimize.brentq(lambda xi: fun(xi), 2, -1, rtol = 10**(-10), full_output = 1)

plt.xlabel("X")
plt.ylabel("Y")
x = np.arange(-1, 2, 0.1)
plt.figure(0)
plt.plot(x,fun(x))
xs = np.linspace(-1,2,100)
horiz_line_data = np.array([0 for i in range(len(xs))])
plt.plot(xs, horiz_line_data, 'r--') 
plt.plot(r1, fun(r1), "ro")

print('Valor de la raiz:',r1)
print('Numero de iteraciones',it)