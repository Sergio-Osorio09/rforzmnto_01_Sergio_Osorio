"""
Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios.
"""
"""
1er metodo:
pida ingresar un nombre y apellido
2do metodo: 
pedir su edad
3ro metodo:
imprima ambos resultados, pero estarán contenidos en un diccionario
"""

class Info:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 0

    def Input_Nom_Ape(self):
        self.nombre = str(input("Ingrese su nombre: "))
        self.apellido = str(input("Ingrese su apellido: "))

    def Input_edad(self):
        self.edad = int(input("Ingrese su edad: "))

    def Out_Info(self):
        info = {"Nombre": self.nombre, "Apellido": self.apellido, "Edad": self.edad}
        print("------------Los resultados:--------------")
        for key, value in info.items():
            print("------------{}-->{}".format(key, value))

persona_0 = Info()

persona_0.Input_Nom_Ape()
persona_0.Input_edad()
persona_0.Out_Info()
