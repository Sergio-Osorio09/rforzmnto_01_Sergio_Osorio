"""
Crea una lista vacía (con 10 posiciones), pide sus valores y devuelve la suma y la media
de los números.
"""
lista = [None] * 10

for i in range(len(lista)):
    valor = float(input("Ingrese el valor {}: ".format(i+1)))
    lista[i] = valor

suma = sum(lista)
media = suma / len(lista)

print("La suma de los números es:", suma)
print("La media de los números es:", media)
