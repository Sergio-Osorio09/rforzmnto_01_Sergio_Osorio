"""
10.Crear un diccionario con los siguientes key: nombre, carrera, edad y año de
nacimiento, mostrar en pantalla el valor de este diccionario.
"""

nombre = str(input("Ingrese nombre: ")).upper()
carrera = str(input("Ingrese carrera: ")).upper()
edad = int(input("Ingrese edad: "))
nacimiento = int(input("Ingrese año de nacimiento: "))

dicc = {"nombre": nombre, "carrera": carrera, "edad": edad, "año de nacimiento": nacimiento}

print(dicc)
