"""Ejercicio 2.15
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""






edades=(10,20,21,30,40,50,10,50,10,100)
conta=0
for a in edades:
    if a > 20:
        conta+=1
print(f"{conta}")