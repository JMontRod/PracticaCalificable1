"""Ejercicio 1.3
Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3
"""

def listar():
    contador=1
    while contador < 10:
        resto = contador

        if resto % 3 ==0:
            print(f"{contador}")
            contador+=1
        else:
            contador+=1
listar()
