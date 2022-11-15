"""Ejercicio 2.11
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.
"""


def mas_larga(Lista_de_palabras):
    palabra_mayor = len(Lista_de_palabras[0])
    palabra_a_mostrar = Lista_de_palabras[0]
    for palabra in Lista_de_palabras:
        if palabra_mayor <= len(palabra):
            palabra_a_mostrar = palabra
            palabra_mayor = len(palabra)
        else:
            palabra_a_mostrar = palabra_a_mostrar

    print(palabra_a_mostrar)


lista = ["a", "patata", "ratastrofico"]
mas_larga(lista)
