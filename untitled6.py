# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:08:20 2022

@author: lab
"""

def suma(*a):
    print("\n tipo de datos del parametro: ",type(a))
    sum=0
    for n in a:
        sum+=n
    print("suma: ",sum)
suma(3)
suma(2)
suma(4)
suma(8)