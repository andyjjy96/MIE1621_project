#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:57:18 2021

@author: Andy
"""


import numpy as np
from numpy import linalg as LA
import sys 

stdoutOrigin=sys.stdout 
sys.stdout = open("log.txt", "w")

f = lambda x: (np.sqrt(x[0]**2+1) + np.sqrt(x[1]**2+1))
dfx1 = lambda x: (x[0]/np.sqrt(x[0]**2+1))
dfx2 = lambda x: (x[0]/np.sqrt(x[1]**2+1))

x0 = np.array([10,10])

#Parameters
alpha = 1
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
    d = - np.array([dfx1(x0),dfx2(x0)])    #steepest descent method  
    while (f(x0) - f(x0 + alpha * d)) < (- gamma * alpha * np.dot(np.transpose(np.array([dfx1(x0),dfx2(x0)])),d)):       
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