
# Online Python - IDE, Editor, Compiler, Interpreter

#Proyecto Melissa Moncayo

import numpy as np
import math
RED='\033[31m'
BLUE='\033[34m'
RESET='\033[39m'
GREEN='\033[32m'
YELLOW='\033[33m'
print(RED+"BIENVENIDOS AL PROGRAMA DE ALGEBRA LINEAL")
print(BLUE+"VECTORES EN R2")
def introduccion(a):
  if a=="si"or a=="SI" or a=="Si":
    print(BLUE+"LOS VECTRORES EN R2: ",end=" ")
    print(RESET+" Los vectores en R2 son aquellos que están ubicados en un plano cartesiano de ejes X e Y")
  else:
    print(RED+"CONTINUE")
a=input(RESET+"Desea conocer definiciones de los VECTORE EN R2: ")
vector=[]
def llenado(n):
  for i in range (n):
    vector.append([0]*n)
  for i in range (n):
    vector[i]=int(input("ingrese el valor {}:".format(i+1)))
  return vector[i]
def myd(vector1,r,acum):
  for i in range(n):
    r=(vector1[i])**2
    acum=acum+r
  return acum

def di(vector1):
  y=vector1[1]/vector1[0]
  x=np.arctan(y)*180/np.pi
  return x
def unitario(vector1):
  for i in range(n):
    print(vector[i],"/",modulo,",",end=" ")

vector2=[]
def suma(vector1,vector2):
  for i in range (n):
    vector2.append([0]*n)
  for i in range (n):
    vector2[i]=int(input("ingrese el valor {}:".format(i+1)))
  print(vector2)
  print("La suma de los vectores es: \n")
  print("[",end=" ")
  for i in range(n):
    t=vector1[i]+vector2[i]
    print(t,end=" ")
  print("]")
vector3=[]
def resta(vector1,vector3):
  for i in range (n):
    vector3.append([0]*n)
  for i in range (n):
    vector3[i]=int(input("ingrese el valor {}:".format(i+1)))
  print(vector3)
  print("La resta de los vectores es: \n")
  print("[",end=" ")
  for i in range(n):
    s=vector1[i]-vector3[i]
    print(s,end=" ")
  print("]")
def escalar(vector1,n):
  print("[",end=" ")
  for i in range(n):
    es=num*vector1[i]
    print(es,end=" ")
  print("]")
introduccion(a)
print()
vector4=[]
def multi(vector1,vector4,acum2,to):
  for i in range (n):
    vector4.append([0]*n)
  for i in range (n):
    vector4[i]=int(input("ingrese el valor {}:".format(i+1)))
  print("El vector es: ")
  print(vector4)
  print("El producto punto de los vectores es: \n")
  for i in range(n):
    s=vector1[i]*vector4[i]
    acum2=acum2+s
  print(acum2)
  print()
  mo=(modulo)**2
  to=(acum2/mo)
  print("la proyección del vector 1 en el vector 2 es:")
  print("[",end=" ")
  for i in range (n):
    total=to*vector1[i]
    print(total,end="   ")
  print("]")
n=2
while True:
  k=input(RESET+"ELIJA UNA OPCIÓN: \n B=Módulo y dirección del vector\n C=Vector unitario\n D=Suma de vectores\n E=Resta de vectore \n F=Producto escalar de un vector\n G=Producto punto de los vectores\n H=Proyección de un vector sobre otro\n")
  print(BLUE+"Ingrese el vector: ")
  print(RESET+" ")
  llenado(n)
  vector1=[0]*n
  vector1=vector
  print("El vector es: \n",vector1)   
  print()
  if k=="B" or k=="b": 
    acum1=myd(vector1,0,0)
    modulo=pow(acum1,1/2)
    print(YELLOW+"El modulo es: ",modulo)
    dir=di(vector1)
    print("la dirección es:",dir)
    print()
  if k=="c" or k=="C":
    acum1=myd(vector1,0,0)
    modulo=pow(acum1,1/2)
    print(BLUE+"El vector unitario es: ")
    u=unitario(vector1)
    print()
  if k=="D" or k=="d":
    print(BLUE+"Igrese el otro vector para realizar la suma: ")
    print(RESET+" ")
    suma(vector1,vector2)
    print()
  if k=="e" or k=="E":
    print(BLUE+"Igrese el otro vector para realizar la resta: ")
    print(RESET+" ")
    resta(vector1,vector3)
    print()
  if k=="f" or k=="F":
    num=int(input((BLUE+"Ingrese el escalar que desea multiplicar: ")))
    print(RESET+" ")
    escalar(vector1,n)
  if k=="g" or k=="G":
    print(BLUE+"Igrese el otro vector para realizar el producto punto: ")
    print(RESET+" ")
    multi(vector1,vector4,0)
  if k=="h" or k=="H":
    acum1=myd(vector1,0,0)
    modulo=pow(acum1,1/2)
    print("la proyección del vector u sobre el v es: ")
    multi(vector1,vector4,0,0)
    print()
  z=input(RED+"Desea salir digite si: ")
  if z=="SI" or z=="si" or z=="Si":
    break
