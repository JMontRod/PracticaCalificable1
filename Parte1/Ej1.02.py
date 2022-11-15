"""Solicitar al usuario dos valores:
● numero1 (int)
● numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
¿Cuál es el código del requerimiento solicitado?"""
num1=int(input())
num2=int(input())

def MAXI(num1,num2):
    if num1>num2:
        print(f"El numero mayor es {num1}, el cual es el 1º numero")
    elif num1<num2:
        print(f"El numero mayor es {num2}, el cual es el 2º numero")
    else:
        print('Los dos valores son iguales')


MAXI(num1,num2)