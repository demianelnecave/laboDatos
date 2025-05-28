import numpy as np
import matplotlib.pyplot as plt

"""
matriz resuelve-sistema
"""
c= -3
b= 11/2
a=-3/2
xx = np.array([1,2,3])
yy = np.array([1,2,0])
x = np.linspace(0, 4, 100)

f = lambda t: a*t**2+b*t+c

plt.plot(xx,yy,'*')
plt.plot(x,f(x))
plt.show()