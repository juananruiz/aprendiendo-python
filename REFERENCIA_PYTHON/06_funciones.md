# Funciones

## Definición básica

```python
def saludar(nombre):
    return f"Hola, {nombre}"

resultado = saludar("Ana")
print(resultado)   # "Hola, Ana"
```

## Parámetros por defecto

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

saludar("Ana")            # "Hola, Ana"
saludar("Ana", "Buenos días")  # "Buenos días, Ana"
```

> Los parámetros con valor por defecto van **siempre al final**.

## Keyword arguments (argumentos por nombre)

```python
def crear_usuario(nombre, edad, ciudad):
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad}

# Puedes llamarlos en cualquier orden si usas el nombre:
crear_usuario(edad=25, ciudad="Madrid", nombre="Luis")
```

## *args y **kwargs

```python
# *args: número variable de argumentos posicionales
def suma(*numeros):
    return sum(numeros)

suma(1, 2, 3)       # 6
suma(1, 2, 3, 4, 5) # 15

# **kwargs: número variable de argumentos por nombre
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=28, ciudad="Madrid")
```

## Retorno de múltiples valores

```python
def minmax(lista):
    return min(lista), max(lista)

minimo, maximo = minmax([3, 1, 4, 1, 5, 9])
# minimo = 1, maximo = 9
```

## Scope: local vs global

```python
x = 10  # variable global

def funcion():
    x = 99  # variable local — no modifica la global
    print(x)

funcion()  # imprime 99
print(x)   # imprime 10 — sin cambios

# Para modificar la global (raro, normalmente señal de mal diseño):
def funcion():
    global x
    x = 99
```

## Funciones lambda (funciones anónimas)

```python
# Útiles para operaciones cortas de una sola expresión
doble = lambda x: x * 2
doble(5)   # 10

# Uso típico: como argumento de sorted, map, filter
nombres = ["Carlos", "Ana", "Beatriz"]
sorted(nombres, key=lambda n: len(n))   # ordena por longitud
# ["Ana", "Carlos", "Beatriz"]

numeros = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, numeros))      # [1, 4, 9, 16, 25]
list(filter(lambda x: x > 2, numeros))  # [3, 4, 5]
```

## Documentar funciones con docstrings

```python
def dividir(a, b):
    """
    Divide a entre b.

    Args:
        a: dividendo
        b: divisor (no puede ser 0)

    Returns:
        Resultado de la división como float.

    Raises:
        ValueError: si b es 0.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b

help(dividir)   # muestra el docstring
```

## Buenas prácticas

- Una función debe hacer **una sola cosa**.
- Si necesita más de 4-5 parámetros, probablemente debería recibir un dict o un objeto.
- Prefer retornar valores antes que modificar variables globales.
- Nómbrala con un **verbo**: `calcular_precio`, `obtener_usuario`, `validar_email`.
