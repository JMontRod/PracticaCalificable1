"""Ejercicio 2.9
Definir un histograma procedimiento() que tome una lista de números enteros e
imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
lo siguiente:"""


lista=[10,10,13,13,18,7]
def procedimiento():
    c =""
    for a in lista:
        for b in range (0,a):
            c=c+"*"
        print(c)
        c=""



procedimiento()