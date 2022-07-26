# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:11:51 2022

@author: lab
"""

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
ubicacion=input("Ingrese su ubicacion: ")
edad=int(input("Ingrese su edad: "))
i=1
space=" "
if i==1:
 while True:
    if edad<5:
        print("es un Bebe")
    else:
        if edad>=5 and edad<12:
            print("es un Niño")
            if edad>=12 and edad<18:
                print("es un Adolescente")
                if edad>=18 and edad<25:
                    print("es un Jóven")
                    if edad>=25 and edad<40:
                        print("es un Adulto jóven")
                        if edad>=40 and edad<50:
                            print("es un Adulto")
                            if edad>=50 and edad<65:
                                print("es un Adulto mayor")
                                if edad>=65 and edad<75:
                                    print("es un Ancianos")
                                    if edad>74:
                                        print("es un Longevos") 
                                        
                                        i=input("si desea continuar ingrese 1")
                                    
                                    
                                        