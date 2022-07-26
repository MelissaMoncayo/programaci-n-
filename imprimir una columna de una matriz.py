# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:34:43 2022

@author: lab
"""

A=[[1,2,3],[4,5,6],[8,"n",9],[1,8,7]]

print()
for fila in A:
    print("[",end=" ") #"imprime el corchete inicial"
    for elemento in fila:
        print("{}".format(elemento), end=" ")
    print("]")   #"imprime el corchete final"
print()
        

#imprime columna i
i=1

columna=[fila[i] for fila in A]
print(columna)