# Listas

## Crear y acceder

```python
lista = [10, 20, 30, 40, 50]

lista[0]    # 10   — primer elemento
lista[-1]   # 50   — último elemento
lista[1:3]  # [20, 30]  — slicing (3 no incluido)
lista[::-1] # [50, 40, 30, 20, 10]  — invertida
```

## Métodos principales

```python
lista = [3, 1, 4, 1, 5]

lista.append(9)         # añade al final → [3, 1, 4, 1, 5, 9]
lista.insert(0, 99)     # inserta en posición 0 → [99, 3, 1, 4, 1, 5, 9]
lista.extend([7, 8])    # añade otra lista al final
lista.pop()             # elimina y devuelve el último
lista.pop(0)            # elimina y devuelve el de posición 0
lista.remove(1)         # elimina la PRIMERA ocurrencia del valor 1
lista.index(4)          # devuelve el índice del valor 4
lista.count(1)          # cuenta cuántas veces aparece 1
lista.sort()            # ordena en el lugar (modifica la lista)
lista.sort(reverse=True)# ordena descendente
lista.reverse()         # invierte en el lugar
lista.clear()           # vacía la lista
copia = lista.copy()    # copia superficial
```

## Funciones globales sobre listas

```python
len(lista)      # número de elementos
sum(lista)      # suma (solo números)
min(lista)      # mínimo
max(lista)      # máximo
sorted(lista)   # devuelve lista ordenada nueva (no modifica la original)
list(range(5))  # [0, 1, 2, 3, 4]
```

## Iterar

```python
for elemento in lista:
    print(elemento)

# Con índice y valor a la vez
for i, valor in enumerate(lista):
    print(f"{i}: {valor}")

# Iterar dos listas a la vez
nombres = ["Ana", "Luis"]
edades  = [25, 30]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

## List comprehensions

```python
# Forma básica: [expresión for elemento in iterable]
cuadrados = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Con filtro
pares = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformar strings
mayusculas = [s.upper() for s in ["hola", "mundo"]]
# ["HOLA", "MUNDO"]
```

## Listas anidadas (matrices 2D)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matriz[1][2]   # 6 — fila 1, columna 2

# Recorrer todos los elementos
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
```

## Errores frecuentes

```python
# IndexError: acceder a índice que no existe
lista = [1, 2]
lista[5]   # IndexError

# Copiar listas: cuidado con la referencia
a = [1, 2, 3]
b = a          # b ES a (misma referencia)
b.append(4)
print(a)       # [1, 2, 3, 4] — ¡a también cambió!

# Solución:
b = a.copy()   # o b = a[:]  o b = list(a)
```
