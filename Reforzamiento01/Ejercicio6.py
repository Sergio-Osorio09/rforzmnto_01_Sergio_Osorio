"""
6.Calcular la media de 5 datos (floats), cada dato debe estar en una variable y la media
también. Mostrar el resultado en pantalla.
"""

datos = []
for i in range(5):
    dato = float(input(f"Ingrese el dato {i+1}: "))
    datos.append(dato)
suma = sum(datos)
media = suma/5

print("La media es: ", "{:.3f}".format(media))