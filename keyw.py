# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:20:21 2022

@author: lab
"""

def keyw(**datos):
    print("\n Tipo de daatos del argumento: ",type(datos))
    for key, value in datos.items():
        print("{}is {}".format(key,value))
        
keyw(firstname="Juan", lastname="Lopez", Age=42, Phone=02156411)
keyw(firstname="Jhon", lastname="Monta", Email="mmoncayo@gmail.com",country="Ecuador",Age=42)