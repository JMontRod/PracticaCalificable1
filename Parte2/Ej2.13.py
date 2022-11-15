"""Ejercicio 2.13
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

mayus=0

cadena = str(input("introduce la cadena de palabras: "))

patata = []
lista = patata.append(cadena)

for a in patata:
    for b in a:
        if b.isupper()== True:
            mayus+=1
print(f"{mayus}")