"""
Ejercicio 2.16
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)
"""

palabra=str(input("Pon palabra: "))

conta=0

patata=["javier","alberto","julian"]
for a in patata:
    if a.startswith(f"{palabra}"):
        conta+=1
print(f"{conta}")
