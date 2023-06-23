"""
Listas copy(): Copia todos los valores de una lista a otra variable
"""

list_1 = ["ale",21,False]
list_2 = list_1.copy()
list_2.append("Lima")
print("El contenido de mi lista es : {}".format(list_1))
print("El contenido de mi nueva lista es : {}".format(list_1))
print("El contenido de mi nueva lista es : {}".format(list_2))
