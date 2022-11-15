"""Ejercicio 2.1
Definir una función max() que tome como argumento dos números y devuelva el mayor
de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
nosotros mismos es un muy buen ejercicio.
"""

num1=int(input())
num2=int(input())


def max(num1,num2):
    if num1>num2:
        print("El numero mayor es el 1º")
    elif num1<num2:
        print("El numero mayor es el 2º")
    else:
        print("Los numeros son iguales")

max(num1,num2)