# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input("ingrese el número de calificaciones: "))
i=1
cont1=0
acum1=0
cont2=0
acum2=0
while i<=n:
    nota=int(input("ingrese la calificación: "))
    i=i+1
    if nota>=0 and nota<=10:
        acum1=acum1+nota
        cont1=cont1+1
    else: 
            acum2=acum2+nota
            cont2=cont2+1
promedioC=acum1/cont1
promedioI=acum2/cont2
print("las notas correctas son: ", cont1)
print("las notas incorrectas son: ", cont2)
print("el promedio de las calificaciones corretas es: ", promedioC)    
print("el promedio de las calificaciones corretas es: ", promedioI)     
        
