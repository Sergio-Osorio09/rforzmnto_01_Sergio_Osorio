"""
Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del.
"""
lista = []

for i in range(1, 16):
    lista.append(2 * i - 1)
lista.insert(4,3.1415)
lista.insert(4,3.1415)
lista.insert(4,3.1415)
print("lista de impares es: ", lista)
lista.insert(4,"cadena")
print("Lista actual: ", lista)
del lista[4]
print("Lista final: ", lista)