"""Ejercicio 2.12
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres."""

def filtrar_palabras(numero,Lista_de_palabra):

        for palabra in Lista_de_palabra:
            if len(palabra) > numero:
                print(f"{palabra}")


nume=8
lista=["patatofono","ratatonico","hola"]
filtrar_palabras(nume,lista)