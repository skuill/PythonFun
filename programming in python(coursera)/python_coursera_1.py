# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:57:47 2017

@author: User
"""

import sys

if (len(sys.argv) > 0):
    digit_string = sys.argv[1]
    if isinstance(digit_string, str) and digit_string:
        digit_list = [int(ch) for ch in digit_string if ch.isdigit()]
        sum_result = sum(digit_list)
        #for i in digit_string:
        #    if i.isdigit():
        #        sum += int(i)
        print (sum_result)
        