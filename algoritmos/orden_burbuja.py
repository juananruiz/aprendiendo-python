
import random
# orden-burbuja.py

# Crea una lista con números aleatorios
# (esta era mi propuesta)
# lista = []
# numero_maximo = 100
# while len(lista) < numero_maximo // 10:
#     elemento = random.randint(1, numero_maximo)
#     if elemento not in lista:
#         lista.append(elemento)
lista = random.sample(range(1, 101), 10) # range excluye el limite superior

cambio = True
vueltas = 0
n = len(lista)
print(lista)

while cambio:
    vueltas += 1
    cambio = False
    for i in range(n - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            cambio = True
print("Desorden: " + str((vueltas - 1) / n - 1))
print(lista)
