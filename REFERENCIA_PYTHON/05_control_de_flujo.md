# Control de flujo

## if / elif / else

```python
edad = 18

if edad < 13:
    print("niño")
elif edad < 18:
    print("adolescente")
elif edad == 18:
    print("recién mayor")
else:
    print("adulto")
```

### Expresión condicional (ternario)

```python
estado = "mayor" if edad >= 18 else "menor"
```

---

## for

Itera sobre cualquier iterable (lista, string, rango, diccionario...).

```python
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8  — paso 2
    print(i)

for letra in "Python":     # itera caracteres
    print(letra)
```

### break, continue, pass

```python
# break — sale del bucle completamente
for i in range(10):
    if i == 5:
        break
    print(i)   # imprime 0, 1, 2, 3, 4

# continue — salta a la siguiente iteración
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # imprime solo impares: 1, 3, 5, 7, 9

# pass — no hace nada, sirve de placeholder
for i in range(5):
    pass   # útil cuando la sintaxis exige un bloque pero aún no tienes código
```

### for / else

El bloque `else` se ejecuta si el bucle terminó **sin** `break`.

```python
numeros = [1, 3, 5, 7]
for n in numeros:
    if n % 2 == 0:
        print("Encontré un par")
        break
else:
    print("No hay ningún número par")  # se ejecuta este
```

---

## while

Repite mientras la condición sea verdadera.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Bucle infinito controlado con break
while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada == "salir":
        break
```

---

## Valores que Python trata como False

```python
# Todos estos son "falsy":
bool(0)        # False
bool(0.0)      # False
bool("")       # False
bool([])       # False
bool({})       # False
bool(None)     # False

# Útil para comprobar si algo está vacío:
lista = []
if not lista:
    print("La lista está vacía")
```

---

## Comparar con `in`

```python
frutas = ["manzana", "pera", "uva"]

if "pera" in frutas:
    print("hay pera")

if "kiwi" not in frutas:
    print("no hay kiwi")
```
