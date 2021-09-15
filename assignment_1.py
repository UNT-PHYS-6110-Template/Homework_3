from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
# setup of the system
# when you need to introduce an arbitrary value, choose 1.
nsites=100
mirror_size=(nsites,nsites)
deposition_rate=1. # number of deposited layers per second 
n_timesteps=1 #total time simulated in seconds
dt=1. #time step in seconds
#
# Initialize state of the system and containers for the simulation results
#
surface_coverage=np.zeros(mirror_size,dtype='int') # initial coverage is a (nx,ny) matrix of zeros
time=np.zeros(n_timesteps)
n_empty_sites=np.zeros(n_timesteps,dtype='int')
#
for i in np.arange(0,n_timesteps,1):
    covered_sites=np.random.randint(0,nsites,(nsites*nsites,2))
    for site in covered_sites:
        surface_coverage[tuple(site)]+=1
    n_covered_sites=np.count_nonzero(surface_coverage)
    time[i]=i*dt
    n_empty_sites[i]=nsites*nsites-n_covered_sites
#
fig = plt.figure()
ax = plt.axes(projection='3d')
x=np.arange(nsites)
y=np.arange(nsites)
X,Y = np.meshgrid(x,y)
ax.contour3D(X, Y, surface_coverage, 50, cmap='Oranges')
plt.show()