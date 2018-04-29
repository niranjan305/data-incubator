#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:38:16 2018

@author: niranjan
"""

import numpy as np

def calc_D(m,n,x,y):
    D = max(((x/m)-(y/n)),((y/n)-(x/m)))
    return D

def walk_north(m,n,x,y):
    if x==m and y<n:
        y+=1
    elif x<m:
        x+=1
    return x,y

def walk_east(m,n,x,y):
    if y==n and x<m:
        x+=1
    elif y<n:
        y+=1
    return x,y

def take_step(m,n,x,y):
    if(np.random.rand()>0.5):
        x,y = walk_north_v(m,n,x,y)
    else:
        x,y = walk_east_v(m,n,x,y)
    return x,y

grid_m = 11
grid_n = 7
D_tot = np.zeros((30,2))
x_tot = np.zeros((30,2))
y_tot = np.zeros((30,2))
x_loc = [10,5]
y_loc = [2,1]

## Vectorized
walk_north_v = np.vectorize(walk_north)
walk_east_v = np.vectorize(walk_east)
take_step_v = np.vectorize(take_step)
calc_D_v = np.vectorize(calc_D)

while np.all(x_loc)<grid_m and np.all(y_loc)<grid_n:
    x_loc,y_loc = take_step_v(grid_m,grid_n,x_loc,y_loc)
    D_tot[i] = calc_D_v(grid_m,grid_n,x_loc,y_loc)
    #x_tot[i] = x_loc
    #y_tot[i] = y_loc
#    D = ((x_loc/grid_m)-(y_loc/grid_n)),((y_loc/grid_n)-(x_loc/grid_m))
    
    #print('X:%d Y:%d' %(x_loc,y_loc))

#D_mean = np.mean(D_tot)
    
#print("%f" % D_mean)
    