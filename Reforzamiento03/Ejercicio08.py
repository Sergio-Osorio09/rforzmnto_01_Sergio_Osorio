"""
Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)
"""


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {"Nombre": nombre, "Telefono": telefono, "Email": email, "dni": dni}
        self.contactos.append(contacto)
        print("Se agrego {} a la agenda".format(contacto))
    def mostrar_contactos(self):
        for contacto in self.contactos:
            print("Nombre: {}".format(contacto["Nombre"]))
            print("Telefono: {}".format(contacto["Telefono"]))
            print("Email: {}".format(contacto["Email"]))
            print("DNI: {}".format(contacto["dni"]))

    def Buscar_contacto(self, dni):
        for contacto in self.contactos:
            if contacto["dni"] == dni:
                print("Nombre: {}".format(contacto["Nombre"]))
                print("Telefono: {}".format(contacto["Telefono"]))
                print("Email: {}".format(contacto["Email"]))
                print("DNI: {}".format(contacto["dni"]))
                return
        print("No se encontro")

agenda = Agenda()
agenda.agregar_contacto("Juan", 12345, "abc@gmail.com", "00000000")
agenda.agregar_contacto("Darly", 28472, "aaaaaaa@gmail.com", "1111111111")
print("--------------------------------------")
agenda.mostrar_contactos()
print("--------------------------------------")
agenda.Buscar_contacto("00000000")
print("--------------------------------------")
agenda.Buscar_contacto("1")



