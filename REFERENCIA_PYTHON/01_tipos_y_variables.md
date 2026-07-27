# Tipos y variables

## Tipos básicos

```python
entero   = 42
decimal  = 3.14
texto    = "hola"
booleano = True       # también False
nada     = None       # ausencia de valor
```

## Comprobar el tipo

```python
type(42)        # <class 'int'>
type("hola")    # <class 'str'>
isinstance(42, int)   # True
isinstance(42, float) # False
```

## Conversión de tipos

```python
int("42")       # 42     — falla si el string no es número
int(3.9)        # 3      — trunca, no redondea
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False  — también es False: None, "", [], {}, 0.0
bool(1)         # True   — cualquier otro valor es True
```

## Números: detalles que sorprenden

```python
un_millon = 1_000_000    # los guiones bajos son solo visuales, ayudan a leer
1_000_000 == 1000000     # True

2e3       # 2000.0  — notación científica (2 × 10³), siempre float
1.5e-2    # 0.015

7 // 2    # 3    división entera
-7 // 2   # -4   ¡ojo! floor redondea hacia abajo, no hacia cero
```

> **Error frecuente**: los `float` no son exactos. Se guardan en binario y
> algunos decimales no tienen representación finita:
>
> ```python
> 0.1 + 0.2          # 0.30000000000000004  ¡no es 0.3!
> 0.1 + 0.2 == 0.3   # False
> round(0.1 + 0.2, 2) == 0.3   # True — compara redondeando
> ```
> Para dinero o precisión exacta, usa `decimal.Decimal` en vez de `float`.
> Ya te topaste con esto en `algoritmos/babylonian_square_root.py`: ahí no
> comparas con `==`, sino con `math.isclose(guess, better_guess)`,
> exactamente por este motivo.

## Redondear vs truncar

```python
int(3.9)      # 3    — trunca (tira la parte decimal)
round(3.9)    # 4    — redondea al entero más cercano
round(3.14159, 2)  # 3.14  — a 2 decimales
round(2.5)    # 2    — ¡redondeo bancario! .5 va al par más cercano
round(3.5)    # 4
```

## Operadores aritméticos

```python
7 + 2    # 9    suma
7 - 2    # 5    resta
7 * 2    # 14   multiplicación
7 / 2    # 3.5  división (siempre float)
7 // 2   # 3    división entera (floor)
7 % 2    # 1    módulo (resto)
7 ** 2   # 49   potencia
```

## Operadores de comparación

```python
5 == 5    # True   igual
5 != 4    # True   distinto
5 > 3     # True   mayor
5 < 3     # False  menor
5 >= 5    # True   mayor o igual
5 <= 4    # False  menor o igual
```

## Operadores lógicos

```python
True and False   # False
True or False    # True
not True         # False
```

## Asignación múltiple y unpacking

```python
a = b = 0             # ambas valen 0
a, b = 1, 2           # a=1, b=2
a, b = b, a           # intercambio sin variable temporal
x, *resto = [1,2,3,4] # x=1, resto=[2,3,4]
```

## Variables: convenciones de nombre

```python
nombre_de_variable = 1    # snake_case — convención Python
CONSTANTE = 3.14159       # mayúsculas para constantes (por convención, no es forzado)
_privado = "interno"      # guion bajo inicial = señal de "no tocar desde fuera"
```

## Igualdad (`==`) vs identidad (`is`)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b   # True  — ¿tienen el mismo contenido?
a is b   # False — ¿son el MISMO objeto en memoria? No, son dos listas distintas
a is c   # True  — c y a apuntan al mismo objeto
```

Regla práctica: usa `==` para comparar valores. Reserva `is` **solo** para
comparar con `None`:

```python
if x is None:      # ✅ correcto
if x == None:      # funciona, pero no es idiomático
```

## Mutable vs inmutable

Algunos tipos se pueden modificar en su sitio (**mutables**) y otros no
(**inmutables**). Es la causa de muchos errores sutiles.

| Inmutables | Mutables |
|------------|----------|
| `int`, `float`, `bool`, `str`, `tuple` | `list`, `dict`, `set` |

```python
# Inmutable: cada "cambio" crea un objeto nuevo
s = "hola"
s.upper()   # devuelve "HOLA", pero s SIGUE siendo "hola"

# Mutable: se modifica el objeto original
lista = [1, 2]
lista.append(3)   # lista ahora es [1, 2, 3], no se creó nada nuevo
```

> **Error frecuente**: como una variable es solo una etiqueta que apunta a un
> objeto, dos etiquetas pueden apuntar al mismo objeto mutable:
>
> ```python
> a = [1, 2, 3]
> b = a          # b NO es una copia, es la misma lista
> b.append(4)
> a              # [1, 2, 3, 4]  ¡a también cambió!
>
> b = a.copy()   # ahora sí, b es una copia independiente
> ```

> **Error frecuente**: confundir `=` (asignación) con `==` (comparación).
