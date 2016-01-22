# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 22:15:44 2016

@author: yidapa
"""

from interest import days
# How many days does it take to double an amount when the
# interest rate is p=1,2,3,...14?
for p in range(1, 15):
    years = days(1, 2, p)/365.0
    print( 'With p=%2d%% it takes %4.1f years to double the amount' %\
    (p, years) )
