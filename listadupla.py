# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:43:58 2022

@author: lab
"""

lista1=[5,5.58,3,"cisco","networking",
        True, False, 12]
tupla1=[5,5.58,3,"cisco","networking",
        True, False, 12]
print(lista1)
print("\n"*2)
print(tupla1)
print("\n"*2)
print(lista1[0])
print("\n"*2)
print(lista1[7])
print("\n"*2)
print(tupla1[0])
print("\n"*2)
print(tupla1[7])
print("\n"*2)
lista1[6]="academy"
tupla1[6]="academy"
len(lista1)
del lista1[6]
print(lista1[7])