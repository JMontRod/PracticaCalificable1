"""Ejercicio 2.2
Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos"""


num1=int(input())
num2=int(input())
num3=int(input())


def max_de_tres(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(f"El 1º numero es el mayor siendo este {num1}")
        elif num1<num3:
            print(f"El 3º numero es el mayor siendo este {num3}")
    elif num2>num1:
        if num2>num3:
            print(f"El 2º numero es el mayor siendo este {num2}")
        elif num2<num3:
            print(f"El 3º numero es el mayor siendo este {num3}")
    else:
        print("Los tres son iguales")


max_de_tres(num1,num2,num3)