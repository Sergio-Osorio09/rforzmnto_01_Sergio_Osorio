"""
Listas del: elimina un valor de la lista enviando una posicion existente
"""

lista_1 = [0, 2, 4, 6, 8, 10, 20]
lista_2 = lista_1.copy()
del lista_2[2]

print("mi lista inicial es: {}".format(lista_1))
print("mi lista actualizada es: {}".format(lista_2))

"""Eliminar el ultimo valor de la lista"""

del lista_1[-1]
print("mi lista actualizada_1 es: {}".format(lista_1))