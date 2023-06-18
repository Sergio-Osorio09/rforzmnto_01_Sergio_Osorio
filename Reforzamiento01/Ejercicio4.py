"""
4.Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe
estar en una variable. Mostrar el volumen por pantalla.
"""

radio = float(input("Ingrese el radio de la esfera: "))
volumen = 4*(3.1416 * radio) / 3

print("El volumen de la esfera es: ", "{:.3f}".format(volumen)) # "{:.'d'f}".format('variable') // d: la cantidad de decimales