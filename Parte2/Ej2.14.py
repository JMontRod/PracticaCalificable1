"""Ejercicio 2.14
Construir un pequeño programa que convierta números binarios en enteros.
"""
def binario_a_decimal(numero_binario):
	numero_decimal = 0

	for posicion, digito in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito) * 2 ** posicion

	return numero_decimal


print(binario_a_decimal('101'))
print(binario_a_decimal('100011'))
print(binario_a_decimal('101011100011101'))