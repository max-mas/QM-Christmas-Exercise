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
    print("Specify time:")
    time = int( input() )
except:
    print("Invalid input. Used defaults: dx = 0.001, dt = 0.01, time = 3")
    dx = 0.001
    dt = 0.01
    time = 3

# calculate spatial and temporal resolution

xres = int( 1/dx )
tres = int( time/dt )

# create wave function at t = 0. boundary conditions!
psi_0 = []
for i in range(xres):
    if i == 0 or i == xres -1:
        psi_0.append(0)
        continue
    x = i / xres
    f = k * x
    ff = complex(0,f)
    psi_0.append( np.exp(ff) * np.exp( -(x-x_0)**2 / (2*sig**2) ) ) 

# plot probability
prob = []
for i in range(xres):
    prob.append( np.abs( psi_0[i] )**2 )
plt.plot(prob)
plt.show()

# declare psi
psi = psi_0

# omegas for t = 0
omega_j0 = []
for i in range(xres):
    if i != 0 and i != xres -1:
        omega_j0.append( -psi_0[i+1] + (2j*dx**2/dt + 2) * psi_0[i] - psi_0[i-1]  )
    elif i == 0:
        omega_j0.append( -psi_0[i+1] + (2j*dx**2/dt + 2) * psi_0[i] )
    elif i == xres -1:
        omega_j0.append( (2j*dx**2/dt + 2) * psi_0[i] - psi_0[i-1]  )

# a
a_j = []
for i in range(xres):
    if i == 0:
        a_j.append( 2 - 2j*dx**2/dt )  
        continue
    a_j.append( 2 - 2j*dx**2/dt - 1/a_j[i-1] )

# b
b_jn = []
b_prev = b_jn
omega_jn = omega_j0
for i in range(tres):
    b_prev = b_jn
    b_jn = []
    psi_prev = psi

    for k in range(xres):
        if k == 0:
            b_jn.append( omega_jn[0] )
            continue
        if i == 0:
            b_jn.append( omega_j0[k] )
            continue
        b_jn.append( omega_j0[k] + b_prev[k-1]/a_j[k-1] )

    # evolve psi
    for k in range(xres):
        if k == 0 or k == xres -1:
            psi[k] = 0
            continue
        psi[k] = a_j[k] * psi_prev[k-1] + b_jn[k]
    omega_prev = omega_jn

    for k in range(xres):
        if k != 0 and k != xres -1:
            omega_j0.append( -psi[k+1] + (2j*dx**2/dt + 2) * psi[k] - psi[k-1]  )
        elif k == 0:
            omega_j0.append( -psi[k+1] + (2j*dx**2/dt + 2) * psi[k] )
        elif k == xres -1:
            omega_j0.append( (2j*dx**2/dt + 2) * psi[k] - psi[k-1]  )

# plot probability
prob = []
for i in range(xres):
    prob.append( np.abs( psi[i] )**2 )
plt.plot(prob)
plt.show()

