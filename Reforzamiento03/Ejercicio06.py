"""
Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)
"""

class Alumno:
    def __init__(self, nombre, apellido, nota_final):
        self.nombre = nombre
        self.apellido = apellido
        self.nota_final = nota_final
    def Imprimir(self):
        print("El/La alumno {} {} tienen {} de nota final".format(self.nombre, self.apellido, self.nota_final))
    def Nota(self):
        if self.nota_final >= 11:
            print("Aprobó con {}".format(self.nota_final))
        else:
            print("Jaló el curso")

alumno_1 = Alumno("Juan", "Sanchez", 12)
alumno_1.Imprimir()
alumno_1.Nota()
print("---------------------------------")
alumno_1 = Alumno("Alessia", "Montenegro", 9)
alumno_1.Imprimir()
alumno_1.Nota()
print("---------------------------------")
alumno_1 = Alumno("Sergio", "Osorio", 20)
alumno_1.Imprimir()
alumno_1.Nota()