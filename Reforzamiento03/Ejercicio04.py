"""Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados por consola."""

def Cuadrados(num_1, num_2):
    for numero in range(num_1, num_2 + 1):
        cuadrado = numero ** 2
        print("El cuadrado de {} es: {}".format(numero, cuadrado))

num_1 = int(input("Ingrese el valor_inicial: "))
num_2 = int(input("Ingrese el valor_final: "))

Cuadrados(num_1, num_2)
