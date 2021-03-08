# imports
import numpy as np
import matplotlib.pyplot as plt

# constants
k = 40
sig = 0.05
x_0 = 0.25

# specify parameters from cmd line
try:
    print("Specify dx:")
    dx = float( input() )
    print("Specify dt:")
    dt = float( input() )
except:
    print("Invalid input. Used defaults: dx = 0.01, dt = 0.01")
    dx = 0.01
    dt = 0.01

# calculate spatial and temporal resolution

xres = int( 1/dx )
tres = int( 1/dt )

# create wave function at t = 0
psi = []
for i in range(xres):
    if i == 0 or i == xres -1:
        psi.append(0)
    x = i / xres
    f = k * x
    ff = complex(0,f)
    psi.append( np.exp(ff) * np.exp( -(x-x_0)**2 / (2*sig**2) ) ) 

# plot psi abs
psiAbs = []
for i in range(xres):
    psiAbs.append( np.abs( psi[i] ) )
plt.plot(psiAbs)
plt.show()
