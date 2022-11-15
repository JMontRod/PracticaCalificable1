"""Ejercicio 2.4
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False.
"""
carac=str(input())

def vocalizador(carac):
    if carac == "a" or carac =="b" or carac == "c" or carac == "d" or carac =="e":
        print("True")
    else:
        print("False")
vocalizador(carac)