"""Ejercicio 2.3
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
que python tiene la función len() incorporada, pero escribirla por nosotros mismos
resulta un muy buen ejercicio.
"""



def longitud(cadena):

    if type(cadena) is not list and type(cadena) is not str:
        return -1

    contador = 0

    for elemento in cadena:
        contador += 1
    return contador


# Probar
cadena = "Esto es una prueba"
print("Longitud de cadena:", longitud(cadena))
