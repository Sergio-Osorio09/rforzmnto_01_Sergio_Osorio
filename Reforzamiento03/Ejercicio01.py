"""
Escribir una clase en python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico.
"""
"""class Numeros:
    def __init__(self):
        self.resultado = 0
        self.num = int(input("Ingrese un valor: "))

    def Calculo_cubo(self):
        self.num = self.num ** 3
        return self.num
    def Calculo_cua_resultado(self):
        self.resultado = self.num ** 2
        return self.resultado
num_0 = Numeros()
print("El cubo de su numero es: {}".format(num_0.Calculo_cubo()))
print("El cuadrado del resultado anterior es: {}".format(num_0.Calculo_cua_resultado()))"""



class Numeros:
    def __init__(self, num):
        self.resultado = 0
        self.num = num

    def Calculo_cubo(self):
        self.num = self.num ** 3
        return self.num
    def Calculo_cua_resultado(self):
        self.resultado = self.num ** 2
        return self.resultado
a = int(input("Ingrese el valor a calcular: "))
num_0 = Numeros(a)
print("El cubo de su numero es: {}".format(num_0.Calculo_cubo()))
print("El cuadrado del resultado anterior es: {}".format(num_0.Calculo_cua_resultado()))