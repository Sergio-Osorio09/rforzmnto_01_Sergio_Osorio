"""
Listas insert(): inserta un elemento de una posicion dada
"""

listas = [10, 50, 80, 22, 100]

listas.insert(1,200)

print("El valor de mi lista actualizada es: {}".format(listas))

listas.insert(len(listas),9)
print("El valor actual de mi lista actualizada es: {}".format(listas))