"""
9.Elevar al exponente de 4 un número que su valor estará asignado a una variable y
luego restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en
pantalla.
"""

num = int(input("Ingrese un numero: "))
expo = pow(num, 4)
resul = expo - (num * 2)
print("El resultado de la operacion es: ", resul)