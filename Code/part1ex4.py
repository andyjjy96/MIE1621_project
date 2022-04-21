#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:31:59 2021

@author: Andy
"""


import numpy as np
from numpy import linalg as LA
import sys 

stdoutOrigin=sys.stdout 
sys.stdout = open("log.txt", "w")

f = lambda x: ((x[0]+x[1])**4 + x[1]**2)
dfx1 = lambda x: (4*(x[0]+x[1])**3)
dfx2 = lambda x: (4*(x[0]+x[1])**3 + 2*x[1])


x0 = np.array([2,-2])

#Parameters
alpha =1
beta = 0.5
count = 1
gamma = 0.5


    
while LA.norm(np.array([dfx1(x0),dfx2(x0)]))/(1+LA.norm(np.array([f(x0)]))) > 10**(-5):

    print("""

########################
###   iteration {}   ###
########################
""".format(count))
    print("Initial point: ", x0)
    d = - np.array([dfx1(x0),dfx2(x0)])
    while (f(x0) - f(x0 + alpha * d)) < (- gamma * alpha * np.dot(np.array([dfx1(x0),dfx2(x0)]),np.transpose(d))):       
       alpha = beta * alpha
    else: 
      alpha = alpha 
    x1 = x0 + alpha * d
    x0 = x1
    
    print("Search Direction:", d,"step length: ", alpha, "New Iterate:" , x0)
   
    count +=1
    if count +1 > 1001:
        break
    else: 
        continue

sys.stdout.close()
sys.stdout=stdoutOrigin