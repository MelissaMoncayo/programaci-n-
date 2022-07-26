# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:54:11 2022

@author: lab
"""
a=int(input("valor inferior"))
b=int(input("valor superior"))
cal=int(input("ingrese la primera nota: "))
i=1
cont1=0
acum1=0
cont2=0
acum2=0
while cal!=0:
    i=i+1
    cal1=int(input("ingrese notas "))
    if cal>=a and cal<=b:
        acum1=acum1+cal
        cont1=cont1+1
    else: 
            acum2=acum2+cal
            cont2=cont2+1
promedioC=acum1/cont1
promedioI=acum2/cont2
print("las notas correctas son: ", cont1)
print("las notas incorrectas son: ", cont2)
print("el promedio de las calificaciones corretas es: ", promedioC)    
print("el promedio de las calificaciones corretas es: ", promedioI)  