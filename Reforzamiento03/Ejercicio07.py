"""
Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas.
"""

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
    def Imprimir(self):
        print("Los datos son:")
        print("{} con {} años de edad y un sueldo de {}".format(self.nombre, self.edad, self.sueldo))
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")
    def Boni(self):
        self.sueldo = self.sueldo * (120 / 100)
        print("Su suelto con la bonificacion es {}".format(self.sueldo))

persona_1 = Persona("Sergio", 21, 3000)
persona_1.Imprimir()
persona_1.Boni()
print("-------------------------------")
persona_2 = Persona("Juan", 40, 20000)
persona_2.Imprimir()
persona_2.Boni()
