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
#plt.plot(prob)
#plt.show()

# initialise psi
psi = []
for i in range(xres):
    psi.append(psi_0[i])

# initialise omega0
omega_0 = []

for i in range(xres):
    if i == 0 :
        omega_0.append(  -psi[i+1] + (2j * dx**2/dt + 2) * psi[i] ) 
        continue
    if i == xres - 1:
        omega_0.append( (2j * dx**2/dt + 2) * psi[i] - psi[i-1] ) 
        continue
    omega_0.append( -psi[i+1] + (2j * dx**2/dt + 2) * psi[i] - psi[i-1] )  

a = []
for i in range(xres):
    if i == 0:
        a.append( 2 - 2j*dx**2/dt )
        continue
    a.append( 2 - 2j*dx**2/dt - 1/a[i-1] )

omega = []
for i in range(xres):
    omega.append(omega_0[i])

for t in range(tres):
    # b
    b = []
    for i in range(xres):
        if i == 0:
            b.append( omega[i] )
            continue
        b.append( omega[i] + b[i-1]/a[i-1] )
    #advance psi
    for i in range(xres):
        if i == xres -1:
            psi[i] = 0
            continue
        psi[i+1] = a[i] * psi[i] + b[i]
    # omega
    for i in range(xres):
        if i == 0:
            omega[i] = -psi[i+1] + (2j * dx**2/dt + 2) * psi[i]
            continue
        if i == xres -1:
            omega[i] = (2j * dx**2/dt + 2) * psi[i] - psi[i-1]
            continue
        omega[i] = -psi[i+1] + (2j * dx**2/dt + 2) * psi[i] - psi[i-1]
    if t == 0:
        prob = []
        for i in range(xres):
            prob.append( np.abs( psi[i] )**2 )
        plt.plot(prob)
        plt.show()
        print(a[0])
        print(a[500])
        print(b[0])

# plot probability
prob = []
for i in range(xres):
    prob.append( np.abs( psi[i] )**2 )
#plt.plot(prob)
#plt.show()


