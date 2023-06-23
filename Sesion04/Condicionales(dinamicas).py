"""Uso del flujo condicional : if"""

var_1 = int(input("Ingrese variable 1: "))
var_2 = int(input("Ingrese variable 2: "))

if var_1 > var_2:
    print("La variable 1 es mayor")
elif var_1 < var_2:
    print("La variable 2 es mayor")
elif var_1 == var_2:
    print("Ambas variables son iguales")
