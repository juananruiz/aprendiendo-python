# Strings

## Crear strings

```python
s = "hola mundo"
s = 'también válido'
s = """varias
líneas"""
```

## f-strings (la forma moderna de formatear)

```python
nombre = "Juan"
edad = 30
print(f"Me llamo {nombre} y tengo {edad} años")
print(f"El doble es {edad * 2}")
print(f"Pi es {3.14159:.2f}")   # dos decimales → "Pi es 3.14"
```

### Mini-lenguaje de formato dentro de las llaves

```python
precio = 1234.5
f"{precio:.2f}"     # "1234.50"   — 2 decimales
f"{precio:,.2f}"    # "1,234.50"  — separador de miles
f"{precio:>10}"     # "    1234.5" — alinear a la derecha en 10 caracteres
f"{precio:<10}"     # "1234.5    " — a la izquierda
f"{precio:^10}"     # "  1234.5  " — centrado
f"{42:03d}"         # "042"        — rellenar con ceros hasta 3 dígitos
f"{0.75:.0%}"       # "75%"        — como porcentaje

x = 7
f"{x=}"             # "x=7"  — atajo para depurar (imprime nombre y valor)
```

## Métodos más usados

```python
s = "  Hola Mundo  "

s.upper()          # "  HOLA MUNDO  "
s.lower()          # "  hola mundo  "
s.strip()          # "Hola Mundo"     — elimina espacios de los extremos
s.lstrip()         # "Hola Mundo  "   — solo izquierda
s.rstrip()         # "  Hola Mundo"   — solo derecha

s.replace("Mundo", "Python")   # "  Hola Python  "
s.strip().startswith("Hola")   # True
s.strip().endswith("Mundo")    # True

"hola mundo".split(" ")        # ["hola", "mundo"]
"hola mundo".split()           # idem, split() sin argumento separa por cualquier espacio

"-".join(["a", "b", "c"])      # "a-b-c"

"hola mundo".count("o")        # 2
"hola mundo".find("mundo")     # 5  (índice donde empieza; -1 si no existe)
"hola mundo".index("mundo")    # 5  (igual pero lanza ValueError si no existe)

"  ".isspace()     # True
"123".isdigit()    # True
"abc".isalpha()    # True
"abc123".isalnum() # True
```

## Mayúsculas, minúsculas y relleno

```python
"hola mundo".capitalize()  # "Hola mundo" — solo la primera letra
"hola mundo".title()       # "Hola Mundo"  — primera de cada palabra
"Hola".swapcase()          # "hOLA"        — invierte may/min

"42".zfill(5)      # "00042"  — rellena con ceros por la izquierda
"abc".center(7, "-")   # "--abc--"
"abc".ljust(6, ".")    # "abc..."
"abc".rjust(6, ".")    # "...abc"
```

## Separar y trocear

```python
"a,b,c".split(",")           # ["a", "b", "c"]
"a,b,c".split(",", 1)        # ["a", "b,c"]  — como máximo 1 corte
"línea1\nlínea2".splitlines() # ["línea1", "línea2"]
"clave=valor".partition("=")  # ("clave", "=", "valor") — siempre 3 partes
```

## Caracteres especiales (escapes) y raw strings

```python
"primera\nsegunda"   # \n = salto de línea
"col1\tcol2"         # \t = tabulación
"comilla \" dentro"  # \" para meter una comilla sin cerrar el string
"barra \\ invertida" # \\ para una barra literal

ruta = r"C:\nombre\test"   # r"..." = raw: los \ no se interpretan
```

## Indexado y slicing

```python
s = "Python"
#    0 1 2 3 4 5
#   -6-5-4-3-2-1

s[0]     # "P"
s[-1]    # "n"  — último carácter
s[2:4]   # "th" — desde índice 2 hasta 3 (4 no incluido)
s[:3]    # "Pyt"
s[3:]    # "hon"
s[::-1]  # "nohtyP" — invertir string
```

## Comprobar si contiene un substring

```python
"Python" in "Aprendo Python"    # True
"Java" not in "Aprendo Python"  # True
```

## Recorrer un string

```python
for letra in "abc":
    print(letra)        # a, b, c (uno por línea)

for i, letra in enumerate("abc"):
    print(i, letra)     # 0 a / 1 b / 2 c

ord("A")   # 65   — código del carácter
chr(65)    # "A"  — carácter a partir del código
```

> **Error frecuente**: los strings son **inmutables**. `s[0] = "p"` lanza `TypeError`.
> Para modificar un string hay que crear uno nuevo.

> **Error frecuente**: concatenar en un bucle con `+=` es lento, porque cada `+`
> crea un string nuevo (son inmutables). Acumula en una lista y usa `join` al final:
>
> ```python
> # ❌ lento con muchos elementos
> resultado = ""
> for palabra in palabras:
>     resultado += palabra + " "
>
> # ✅ idiomático y rápido
> resultado = " ".join(palabras)
> ```
