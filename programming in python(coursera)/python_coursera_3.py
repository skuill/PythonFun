# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:25:22 2017

@author: User
"""

import sys

if (len(sys.argv) > 0):
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    D = (b**2 - 4*a*c)**0.5
    if (a != 0):
        x1 = (-b + D)/(2*a)
        x2 = (-b - D)/(2*a)
        print (int(x1))
        print (int(x2))
    else:
        print ("a == 0. error")