"""
Ejercicio 2.17
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""


vocal=str(input("Ponga una palabra: "))
def contar_vocales():
    vocalo = vocal.count("o")
    print(f"Hay {vocalo} o")
    vocale = vocal.count("e")
    print(f"Hay {vocale} e")
    vocala = vocal.count("a")
    print(f"Hay {vocala} a")
    vocali = vocal.count("i")
    print(f"Hay {vocali} i")
    vocalu = vocal.count("u")
    print(f"Hay {vocalu} u")


contar_vocales(vocal)