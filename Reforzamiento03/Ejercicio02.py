"""
Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola.
"""

class ReverseDeCadena:
    def __init__(self, cadena):
        self.cadena_actual = cadena

    def revertir_cadena(self):
        palabras = self.cadena_actual.split()
        palabras_revertidas = palabras[::-1]
        self.cadena_actual = ' '.join(palabras_revertidas)
        return self.cadena_actual



a = "Hola Pythonista, seguimos adelante"
reversor = ReverseDeCadena(a)


reversor.revertir_cadena()
print("La cadena revertida es: {}".format(reversor.cadena_actual))

reversor.revertir_cadena()
print("La cadena revertida por 2da vez es: {}".format(reversor.cadena_actual))



