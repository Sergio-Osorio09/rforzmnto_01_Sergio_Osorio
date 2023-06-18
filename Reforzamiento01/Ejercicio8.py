"""
8.Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista vacía.
"""

lista_1 = []
lista_2 = [1, 4, "blablabla", ["a","b"]]

if len(lista_1) == 0:
    print("La lista 1 está vacía")
else:
    print("La lista 1 no está vacía")

if len(lista_2) == 0:
    print("La lista 2 está vacía")
else:
    print("La lista 2 no está vacía")