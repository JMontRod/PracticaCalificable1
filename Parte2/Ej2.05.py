"""Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
lista=[1,2,3,4]
def sum(lista):
    suma=0
    for b in lista:
        suma+=b
    print(f"Esta es la suma: {suma}")

def multi(lista):
    multiplicacion = 1
    for b in lista:
        multiplicacion *= b
    print(f"Esta es la multiplicación: {multiplicacion}")


sum(lista)
multi(lista)
