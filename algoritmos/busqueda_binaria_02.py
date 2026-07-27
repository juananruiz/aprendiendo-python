# busqueda_binaria_02.py
# version 02 - 26 junio 2026

import random

n = 10
lista = random.sample(range(1, n * 10), n)
lista.sort()

numero = int(input(f"Introduce un número del 1 al {n * 10} para buscarlo en la lista: "))

min = 0
max = n 
while min <= max:
	posicion = (min + max) // 2
	if numero == lista[posicion]:
		print("Número encontrado")
		break
	elif numero > lista[posicion]:
		min = posicion + 1
	else:
		max = posicion - 1
else: 
	print("No se ha encontrado el elemento en la lista")

print(lista)