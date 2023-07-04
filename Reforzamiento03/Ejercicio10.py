"""
Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)
"""
#Debe tener descargado "agenda_modulo.py" para poder correr el programa
import agenda_modulo

nombre, apellido = agenda_modulo.ingresar_nombre_apellido()
print("Nombre:", nombre)
print("Apellido:", apellido)

tipo_seguro = agenda_modulo.pedir_tipo_seguro()
print("Tipo de seguro:", tipo_seguro)

es_mayor_edad = agenda_modulo.verificar_mayor_edad()
if es_mayor_edad:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
