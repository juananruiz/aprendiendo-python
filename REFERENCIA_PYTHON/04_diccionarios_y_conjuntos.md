# Diccionarios, conjuntos y tuplas

---

## Diccionarios

Asocian **clave → valor**. Las claves deben ser únicas e inmutables.

```python
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid",
}

# Acceder
persona["nombre"]           # "Ana"
persona.get("email")        # None — no lanza error si no existe
persona.get("email", "N/A") # "N/A" — valor por defecto

# Añadir o modificar
persona["email"] = "ana@example.com"
persona["edad"] = 29

# Eliminar
del persona["ciudad"]
valor = persona.pop("edad")   # elimina y devuelve el valor

# Comprobar si existe una clave
"nombre" in persona    # True

# Iterar
# Solo imprime las claves
for clave in persona:
    print(clave)


for clave, valor in persona.items():
    print(f"{clave}: {valor}")

for valor in persona.values():
    print(valor)
```

### Métodos útiles

```python
persona.keys()    # dict_keys(["nombre", "email"])
persona.values()  # dict_values(["Ana", "ana@..."])
persona.items()   # dict_items([("nombre","Ana"), ...])
persona.update({"ciudad": "Barcelona", "edad": 30})  # actualiza varios a la vez
{}               # diccionario vacío
```

### Diccionario por comprensión

```python
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Diccionarios anidados

```python
usuarios = {
    "ana": {"edad": 28, "activo": True},
    "luis": {"edad": 35, "activo": False},
}
usuarios["ana"]["edad"]   # 28
```

---

## Conjuntos (set)

Sin orden, sin duplicados. Útiles para operaciones de conjuntos y eliminar duplicados.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # {1, 2, 3, 4, 5, 6}  — unión
a & b    # {3, 4}               — intersección
a - b    # {1, 2}               — diferencia (en a pero no en b)
a ^ b    # {1, 2, 5, 6}         — diferencia simétrica

a.add(10)
a.remove(1)    # lanza KeyError si no existe
a.discard(99)  # no lanza error si no existe

# Eliminar duplicados de una lista
lista = [1, 2, 2, 3, 3, 3]
sin_dup = list(set(lista))   # [1, 2, 3] — ojo: pierde el orden
```

---

## Tuplas

Como listas pero **inmutables**. Más rápidas, usadas para datos que no deben cambiar.

```python
punto = (3, 7)
colores = ("rojo", "verde", "azul")

colores[0]      # "rojo"
colores[-1]     # "azul"
len(colores)    # 3

# Unpacking
x, y = punto
r, g, b = colores

# Tupla de un solo elemento (la coma es obligatoria)
uno = (42,)   # sin coma sería solo un int entre paréntesis
```

### Cuándo usar qué

| Estructura | Mutabilidad | Orden | Duplicados | Uso típico |
|------------|-------------|-------|------------|------------|
| `list`     | Mutable     | Sí    | Sí         | Colección que cambia |
| `tuple`    | Inmutable   | Sí    | Sí         | Coordenadas, retorno múltiple |
| `set`      | Mutable     | No    | No         | Pertenencia rápida, eliminar dup. |
| `dict`     | Mutable     | Sí*   | Claves: No | Mapear clave→valor |

> *Los dicts mantienen orden de inserción desde Python 3.7.
