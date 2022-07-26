# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:55:49 2022

@author: lab
"""

h=[['a','b','c'],['d','e','f'],['g','h','i']]
print()
for fila in h:
    print("[",end=" ") #"imprime el corchete inicial"
    for columna in fila:
        print("{}".format(columna), end=" ")
    print("]")   #"imprime el corchete final"
print()
i=0

columna=[fila[i] for fila in h]
print(columna)
j=1

fila=[columna[j] for columna in h]
print(fila)