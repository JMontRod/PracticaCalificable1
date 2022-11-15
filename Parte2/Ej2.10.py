"""
Ejercicio 2.10
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio
2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos
más de 3 números o no sabemos cuántos números son. Escribir una función
max_in_list() que tome una lista de números y devuelva el más grande.
"""

Numeros = [10, 20, 30, 21,300,1999]

def max_in_list():
    maxi=0
    for a in Numeros:
        if maxi<a:
            maxi = a

    print(f"{maxi}")

max_in_list()
