def ingresar_nombre_apellido():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    return nombre, apellido

def pedir_tipo_seguro():
    tipo_seguro = input("Ingrese el tipo de seguro que tiene: ")
    return tipo_seguro

def verificar_mayor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        return True
    else:
        return False