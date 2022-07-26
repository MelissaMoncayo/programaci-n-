i=1
mult=0
tabla=0
acu=0
cont=0
cont2=0
a=int(input("hata que tabla quiere ver: "))
while True:
    if a<1 and a>100:
        print("el numero esta fuera del rango ")
    else:
        break
for m in range (1,a+1):
    cont=0
    cont2=0
    contpar=0
    contimpar=0
    tabla=tabla+1
    print("Tabla del ",tabla)
    for i in range(1,15+1):
        mult=i*tabla
        if (mult%5)==0: 
            cont2=1+cont2
        if (mult%3)==0:
            cont=cont+1
        if (mult%2)==0:
            contpar=contpar+1
        if (mult%2)==1:
            contimpar=contimpar+1
        print(tabla,"*",i,"=",mult)
        acu=acu+mult
        i=i+1
    print("La suma de la tabla ",tabla, "=",acu)  
    print("El promedio de la tabla ",tabla, "=", acu/15)
    print("los multiplos de 3 son: ", cont)
    print("los multiplos de 5 son: ", cont2)
    print("los pares son: ", contpar)
    print("los impares son: ", contimpar)
    print( )
       
    