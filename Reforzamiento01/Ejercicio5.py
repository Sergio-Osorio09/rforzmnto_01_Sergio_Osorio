"""
5.Crear un programa que partiendo de un sueldo en una variable, sepamos si es par o
impar. Utilizar módulo y condicional.
"""

sueldo = float(input("Ingrese sueldo: "))

if sueldo%2 == 0:
    print("Su sueldo es par")
else:
    print("Su sueldo es impar")