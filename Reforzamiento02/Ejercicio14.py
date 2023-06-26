"""
Elimina un elemento por dos índices existentes y ya no por el valor.
"""
lista = [10, 20, 30, 40, 50]

indice_inicio = 1
indice_fin = 3

for _ in range(indice_fin - indice_inicio + 1):
    lista.pop(indice_inicio)

print(lista)