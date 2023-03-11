#Juan Esteban Clavijo García - 202225709
#Problema 2.

palabras=list()

a=1
while a==1:
    palabra=input("Digite una palabra:")
    palabras.append(palabra)
    a=int(input("¿Desea ingresar otra palabra? (1-Sí,2-No):"))
menor5=list()
mayori5=list()
a=0
e=0
i=0
o=0
u=0
for elemento in palabras:
    if len(elemento)<5:
        menor5.append(elemento)
    else:
        mayori5.append(elemento)
    x=elemento.count("a")
    a=a+x
    x=elemento.count("e")
    e=e+x
    x=elemento.count("i")
    i=i+x
    x=elemento.count("o")
    o=o+x
    x=elemento.count("u")
    u=u+x

print("")
print("Palabras de longitud menor a 5:",menor5)
print("Palabras de longitud mayor o igual a 5:",mayori5)
print("Cantidad de veces que aparece la a:",a)
print("Cantidad de veces que aparece la e:",e)
print("Cantidad de veces que aparece la i:",i)
print("Cantidad de veces que aparece la o:",o)
print("Cantidad de veces que aparece la u:",u)
