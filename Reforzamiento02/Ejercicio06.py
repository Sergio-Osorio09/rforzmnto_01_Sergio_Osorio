"""
Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)
dentro de la lista.
"""
lista = ["Calculo infinitesimal", "Flujo Laminar", "Introduccion a Desarrollo de Software",
         "Algebra y geometría analítica II", "Flujo Laminar", "Flujo Laminar"]
print("Elige un curso a calcular la cantidad de repeticiones", "Algebra y geometría analítica II")
print("--------------------------------------------")
print("----------Elija un curso--------------------")
print("--------------------------------------------")
print("----A :Calculo infinitesimal----------------")
print("----B :Flujo Laminar------------------------")
print("----C :Introduccion a Desarrollo de Software")
print("----D :Algebra y geometría analítica II-----")

var = str(input("Introduzca valor [A/B/C/D] :")).upper()
if var == "A":
    print("El curso {} se repite {}".format("Calculo infinitesimal", lista.count("Calculo infinitesimal")))
elif var == "B":
    print("El curso {} se repite {}".format("Flujo Laminar", lista.count("Flujo Laminar")))
elif var == "C":
    print("El curso {} se repite {}".format("Introduccion a Desarrollo de Software", lista.count("Introduccion a Desarrollo de Software")))
elif var == "D":
    print("El curso {} se repite {}".format("Algebra y geometría analítica II", lista.count("Algebra y geometría analítica II")))