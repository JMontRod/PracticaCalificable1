"""Ejercicio 1.1
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor desconocido
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""
print('Pon nota:')
nota=int(input())
def Notas(nota):
    if nota in range(9,11):
        print('A')
    elif nota in range(8,9):
        print('B')
    elif nota in range(7,8):
        print('C')
    elif nota in range(6,7):
        print('D')
    elif nota <6:
        print('C')
    else:
        print('Valor no valido')
Notas(nota)
