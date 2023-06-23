"""Uso del flujo condicional : if"""

edad = int(input("Ingrese su edad: "))

if 0 < edad < 18:
    print("Usted es menor de edad")
elif 18 <= edad <=65:
    print("Usted es mayor de edad")
elif 100 >= edad >65:
    print("Usted es adulto mayor")
else:
    print("Usted ha ingresado una edad incorrecta")