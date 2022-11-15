"""Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
cadena="Estoy patateando"

def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    print(f"{cadena_invertida}")


invertir_cadena_manual(cadena)