# Algoritmo de búsuqeda binaria
# Versión 01 - 24 junio 2026

# Implementa un algoritmo de búsqueda binaria con Python
# 1. Crea una lista de 25 números aleatorios del 1 al 100
# 2. Ordena la lista de números de menor a mayor
# 3. Implementa un algoritmo que comprueba si un número concreto propuesto por el usuario existe

import random

# Crea  la lista con n números aleatorios
n = 100

# lista = []
# while len(lista) < n:
#     elemento = random.randint(1, n * 10)
#     if elemento not in lista:
#         lista.append(elemento)

lista = random.sample(range(1, n * 10), n)
# Casos que habría que testear
# - lista vacía - OK - comprobación previa
# - lista de un solo elemento - OK
# - lista de dos elementos OK
# - lista de tres elementos - OK
# - todos los elementos de la lista son iguales - OK
# - los elementos de la lista no son compatibles con el elemento buscado
#  -He probado a generar 100.000 números un poco lento pero funciona
# 		Tarda unos 38 seg en generar la lista pero busqueda de 3 numeros es inmediata

if len(lista) == 0:
    print("La lista está vacía")

# Ordeno la lista usando las funciones de python
lista.sort()

# lista = [1,1,1,1,1,1,1,1]

# Pregunto al usuario tres números del 1 al 100
entrada = input(f"Escribe tres números del 1 al {n * 10} separados por espacios:")
numeros = [int(x) for x in entrada.split(" ")]
# print(numeros)

# Ahora hago la busqueda binaria
for numero in numeros:
    pos_inferior = 0
    pos_superior = len(lista)
    numero_encontrado = False
    while pos_superior > pos_inferior:
        posicion = (pos_superior + pos_inferior) // 2
        if numero == lista[posicion]:
            numero_encontrado = True
            break
        elif numero > lista[posicion]:
            pos_inferior = posicion + 1
        elif numero < lista[posicion]:
            pos_superior = posicion
    if numero_encontrado:
        print("Número encontrado: " + str(numero))
    else:
        print("Número NO encontrado: " + str(numero))

print(lista)