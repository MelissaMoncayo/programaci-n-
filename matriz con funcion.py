# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:30:03 2022

@author: lab
"""

A=[[1,2,3],[4,5,6],[8,"n",9],[1,8,7]]
B=[[1,2,3,"h"],[4,5,6,7]]
C=[[1,2,3,5,4],[4,5,6,2,1],[8,"n",9,0,0],[1,8,7,2,4]]

def imprime(A):
    print()
    for fila in A:
        print("[",end=" ") #"imprime el corchete inicial"
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")   #"imprime el corchete final"
    print()
imprime(A)
imprime(B)
imprime(C)