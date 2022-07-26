# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
while True:
    x=int(input("ingrese un el primer número: "))
    y=int(input("ingrese un el segundo número: "))
    if x==y:
        print("eror los números con iguales")
        
    else:
        print("los numeros: ",x, "y",y , "son el intervalo ingrese números dentro del intervalo")
        break
if x>y :
    mini=y
    maxi=x
else:
    mini=x
    maxi=y
acum=0
cant=0
suma=0
cont=0
contt=0
n=1
while n!=0:
    n=int((input("ingrese un Número: "))) 
    acum=1+acum
    print("puedo continuar")

    if n==y or n==x:
         cant=1+cant
    elif n>mini and n<maxi:
        suma=n+suma
    else:
        cont=1+cont
        contt=n+contt
cont=cont-1
prom1=contt/cont
print("la suma de los números dentro del intervalo son: ",suma)
print("El promedio de los números fuera del intervalo son: ",prom1) 
print("la cantidad de  números iguales al del intervalo son: ",cant)  
       
