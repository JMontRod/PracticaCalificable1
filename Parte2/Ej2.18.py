"""
Ejercicio 2.18
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""
año=int(input("Pongame un año: "))
def es_bisiesto(año):
    if año % 4 != 0:
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 != 0:  # divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:  # divisible entre 4 y 100 y no entre 400
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:  # divisible entre 4, 100 y 400
        print("Es bisiesto")


es_bisiesto(año)
