"""Ejercicio 2.8
Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver
"xxxxx"""

def generar_n_caracteres(num,letra):
    nume=0
    patata=""
    while nume<num:

       patata+=letra
       nume+=1
       if nume==num:

        return patata


print("La cadena es:", generar_n_caracteres(6,"a"))