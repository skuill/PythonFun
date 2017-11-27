# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:18:28 2017

@author: User
"""

import sys

if (len(sys.argv) > 0):
    digit_string = sys.argv[1]
    if isinstance(digit_string, str) and digit_string and digit_string.isdigit():
        digit = int(digit_string)
        for i in range(1, digit + 1):
            print (" "*(digit - i) + "#"*i)
            