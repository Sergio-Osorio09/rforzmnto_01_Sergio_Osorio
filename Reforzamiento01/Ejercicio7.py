"""
7.De 3 números asignados (tú los propones) a 3 variables se pide hallar la suma de los
valores de los módulos con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la
suma.
"""

var_1 = 15
var_2 = 20
var_3 = 75

var_1 = var_1 % 4
var_2 = var_2 % 9
var_3 = var_3 % 7

print("La suma de los modulos es: ", var_1 + var_2 + var_3)
