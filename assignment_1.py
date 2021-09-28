#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 3
Assignment 1
The following is a program to simulate the random deposition of atoms on the surface of a 
substrate (mirror). The surface is modelled as a square grid and adsorption on each site 
is random and independent on the number of deposited atoms on the other sites. 

Authors: O. Andreussi and STUDENT
"""
# 
# Parameters and variables
# 
# nx, ny : number of adsorption sites along the x and y directions
# n_sites : total number of adsorption sites on the surface
# deposition_rate : number of deposited layers per second
# n_timesteps : number of simulated timesteps, where each timestep correspond
#               to the adsorption of a single atom on the surface.
# surface_coverage : collects the number of adsorbed atoms on each surface site
#
# Import useful modules
#
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
#
# Setup of the system
# when you need to introduce an arbitrary value, choose 1.
#
nx=100 # number of atomic sites along the x direction
ny=100 # number of atomic sites along the y direction
mirror_shape=(nx,ny) # shape of the mirror
n_sites=nx*ny # total number of adsorption sites
deposition_rate=1.0 # number of deposited layers per second 
n_timesteps=100000 #total number of timesteps
dt=1./(deposition_rate*n_sites) #time between single atom adsorptions in seconds
#
# Initialize state of the system and containers for the simulation results
#
surface_coverage=np.zeros(mirror_shape,dtype='int') # initial coverage is a (nx,ny) matrix of zeros
time=np.zeros(n_timesteps)
n_empty_sites=np.zeros(n_timesteps,dtype='int')
#
# Perform the simulation, we add one atom at a time to a randomly picked adsorption site
# on the surface of the mirror
#
for i in np.arange(0,n_timesteps,1):
    adsorption_site=(np.random.randint(0,nx),np.random.randint(0,ny)) # pick a random site on the surface
    surface_coverage[adsorption_site]+=1 # add an atom to the site
    n_covered_sites=np.count_nonzero(surface_coverage) # count how many sites have at least one adsorbed atom
    # here we save the time and the number of empty sites
    time[i]=i*dt
    n_empty_sites[i]=n_sites-n_covered_sites
#
# What is the distribution of the atoms per site?
# in the following we plot the frequency distribution of the surface coverage
# and compare it with an analytical result
#
min_coverage=np.min(surface_coverage)
max_coverage=np.max(surface_coverage)
bins=np.arange(min_coverage,max_coverage+1)
plt.hist(surface_coverage.reshape(n_sites,1),density=True,bins=bins,histtype='step')
alpha=1/n_sites*n_timesteps
p=np.random.poisson(alpha,1000000)
plt.hist(p,density=True,bins=bins,histtype='step')
gaussian=1/np.sqrt(2*np.pi*alpha)*np.exp(-(bins-alpha)**2/2.0/alpha)
plt.plot(bins,gaussian)
plt.show()
# 
# The following lines will generate a graph of the number of empty sites 
# as a function of time
#
plt.plot(time,n_empty_sites)
n_empty_sites_analytical=np.exp(-deposition_rate*time)*n_sites
plt.plot(time,n_empty_sites_analytical)
plt.show()
#
# The following lines will generate a 2D plot of the surface, with darker colors
# corresponding to more adsorbed atoms
#
plt.matshow(surface_coverage,cmap='Oranges')
plt.show()
#
# The following lines will generate a 3D visualization of the surface
# you need to uncomment them (i.e. remove the # symbol at the beginning of the line)
#
#from mpl_toolkits import mplot3d
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#x=np.arange(nx)
#y=np.arange(ny)
#X,Y = np.meshgrid(x,y)
#ax.contour3D(X, Y, surface_coverage, 50, cmap='Oranges')
#plt.show()
