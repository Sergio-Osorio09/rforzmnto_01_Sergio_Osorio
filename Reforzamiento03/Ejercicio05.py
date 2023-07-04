"""
Crear una clase llamada círculo que contenga radio en su constructor y
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.

Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""

class Circulo:
    def __init__(self):
        self.radio = None
        while self.radio is None:                         #Validacion si el dato ingresado es un int
            radio = input("Ingrese radio: ")
            if radio.isdigit():
                self.radio = int(radio)
            else:
                print("Debe ingresar un numero!")

    def Area(self):
            area = 3.1416 * (self.radio ** 2)
            print("El area es: {}".format(round(area, 3))) #round(el valor, el numero de decimales)
    def Perimetro(self):
        per = 2 * 3.1416 * self.radio
        print("El perimetro es: {}".format(round(per, 3)))

a = Circulo()
a.Area()
a.Perimetro()

