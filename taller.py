
"""
edad=int(input("ingrese la edad:"))
dentroDeaños=int(input("ingrese la cantidad de años "))
total=dentroDeaños+edad
print(f"tendras {total} años dentro {dentroDeaños}")


#2

lado=int(input("ingresa un lado del cubo:"))
total=lado**3
print(f"el valor es {total}")


#3

producto=int(input("ingrese el valor del prducto:"))
total= producto + ( producto* 0.19 )
print(f"{producto} + iva total {total}")


#4

producto=int(input("ingrese el valor del prducto:"))
total=  producto -  ( producto* 0.10 )
print(f"{producto} + iva total {total}")


#5

producto=input("ingresa el producto:")
if producto == "crema" or producto == "vino":
    print(f"el si tiene iva {producto}")
elif producto == "arroz" or producto ==  "lentejas":
    print(f"no tiene iva {producto} ")
else:
    print("no es valido")

#6

num1=int(input("ingresa un numero"))
num2=int(input("ingresa un numero"))
if num1>num2:
    print(f"el numero es mayor{num1}")
elif num1<num2:
    print(f"el numero es menor {num1}")     
else:
    print("son iguales")

#7

lado1=int(input("ingrese un angulo"))
lado2=int(input("ingrese un angulo"))
lado3=int(input("ingrese un angulo"))
total=lado1+lado3+lado2
if total == 180:
    print("angulo")
else:
    "es valido"



#8

numero=int(input("ingrese un numero"))
if numero>0:
    if numero%2 == 0:
        print("el numero es par")
    else:
        print("el numero es impar")
else:
    print ("numero es negativo")
---------------------------------------------
num1=int(input("ingrese el numero"))
num2=int(input("ingrese el numero"))
contador=0
while num1 <= num2:
    contador+=num1
    num1+=1
print(contador)

----------------------------------------------------
tabla=int(input("ingresa el numero "))
for i in range(1,11):
    resultado=tabla*i
    print(f"{tabla}x{i}={resultado}")

--------------------------------------------------------
i=1
while i <= 10 :
    print(i)
    i+=2

------------------------------------------------------------
i=0
while i <=3:
    clave=input("desea salir =si , desea seguir =no ")
    print("sigue intentado")
    if clave == "si":
        print("gracias ")
        break
--------------------------------------------------------------------
contador=0
for i in range(5):
    numeros=int(input("ingrese los numeros "))
    contador+=numeros
    print(contador/5)
-----------------------------------------------

ciudad=["toronto" , "Cali" , "paris " , "Pereira" , "buenos aires"]
for i in ciudad:
    if i == "Cali" or i == "Pereira":
        print(i)
-----------------------

"""
i=0
while i<=3:
    print("--------------")
    i+=1
    f=0
    while f <= 5:
        print(i, "x" , f , "=" , i*f )
        f+=1


