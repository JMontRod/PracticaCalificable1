"""Ejercicio 2.7
Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
el bucle for anidado.
"""
prime=[1,4,2,5,8]
segun=[1,4,2,5,9]

def superposicion(prime,segun):
    nume=0
    for a in prime:
        for b in segun:
            if a==b:
                nume=1


            else:
                break

    if nume==0:
        print("False")
    else:
        print("True")

superposicion(prime,segun)