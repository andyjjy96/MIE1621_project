#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:10:56 2021

@author: Andy
"""

import numpy as np
from numpy import linalg as LA

f = lambda x: (x[0]**2 + x[1]**2 + x[2]**2)
dfx1 = lambda x: (2*x[0])
dfx2 = lambda x: (2*x[1])
dfx3 = lambda x: (2*x[2])

x0 = np.array([1,1,1])

#Parameters
alpha = 1
beta = 0.5
count = 1
gamma = 0.5


    
while LA.norm(np.array([dfx1(x0),dfx2(x0),dfx3(x0)]))/(1+LA.norm(np.array([f(x0)]))) >= 10**(-5):
    print("""

########################
###   iteration {}   ###
########################
""".format(count))
    print("Initial point: ", x0)
    d = - np.array([dfx1(x0),dfx2(x0),dfx3(x0)])
    
    while (f(x0) - f(x0 + alpha * d)) < (- gamma * alpha * np.dot(np.transpose(np.array([dfx1(x0),dfx2(x0),dfx3(x0)])),d)):       
       alpha = beta * alpha
    else: 
      alpha = alpha 
    x1 = x0 + alpha * d
    x0 = x1
    
    print( "Search Direction:", d,"step length: ", alpha, "New Iterate:" , x0)
    count +=1
    if count +1 > 1001:
        break
    else: 
        continue