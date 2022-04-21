#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:00:10 2021

@author: Andy
"""
import numpy as np
from numpy import linalg as LA
from numpy.linalg import inv
#import sys 

#stdoutOrigin=sys.stdout 
#sys.stdout = open("log.txt", "w")

f = lambda x: (100*x[0]**4 + 0.01*x[1]**4)
dfx1 = lambda x: (400*x[0]**3)
dfx2 = lambda x: (0.04*x[1]**3)
hx11 = lambda x: (1200*x[0]**2)
hx12 = lambda x: (0)
hx21 = lambda x: (0)
hx22 = lambda x: (0.12*x[1]**2)

#parameters 
alpha = 1
count = 1

#initial point
x0 = np.array([1,1])


while LA.norm(np.array([[dfx1(x0),dfx2(x0)]])) > 10**(-6):
                        
    print("""

########################
###   iteration {}   ###
########################
""".format(count))
    print("Initial point: ", x0)
    d = -np.dot(np.array([dfx1(x0),dfx2(x0)]), inv(np.array([[hx11(x0),hx12(x0)],
                       [hx21(x0),hx22(x0)]])))
                        
    x0 = x0 + alpha * d
    count += 1
    print("Search Direction:", d,"New Iterate:" , x0)

#sys.stdout.close()
#sys.stdout=stdoutOrigin                     