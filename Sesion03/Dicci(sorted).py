"""
sorted
"""

varDiccionario = {"nombre":"Mysql","tipo":"BD relacional"}

"""Obteniendo solamente los valores de los keys o columnas"""

keys = sorted(varDiccionario)
print(keys)

valores = list(varDiccionario.values())
print(valores)
print(valores)

keys_2 = list(varDiccionario.keys())
print(keys_2)

"""Convertir diccionario a una lista"""
lista_convertida = list(varDiccionario.items())
print(lista_convertida)