# Ficheros

## Leer un fichero de texto

```python
# Forma recomendada: con "with" (cierra el fichero automáticamente)
with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()       # todo el contenido como un string

# Leer línea por línea (eficiente con ficheros grandes)
with open("datos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())   # strip() elimina el \n del final

# Leer todas las líneas como lista
with open("datos.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()     # ["línea 1\n", "línea 2\n", ...]
```

## Escribir en un fichero de texto

```python
# "w" — crea el fichero o lo sobreescribe si ya existe
with open("salida.txt", "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")

# "a" — añade al final sin borrar el contenido existente
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nueva entrada de log\n")
```

## Modos de apertura

| Modo | Significado |
|------|-------------|
| `"r"` | Lectura (por defecto). Error si no existe. |
| `"w"` | Escritura. Crea o sobreescribe. |
| `"a"` | Append. Crea o añade al final. |
| `"x"` | Creación exclusiva. Error si ya existe. |
| `"b"` | Modo binario (combinar: `"rb"`, `"wb"`). |

---

## CSV

```python
import csv

# Leer CSV
with open("datos.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)   # cada fila es un diccionario
    for fila in lector:
        print(fila["nombre"], fila["edad"])

# Escribir CSV
personas = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 35},
]
with open("salida.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "edad"])
    escritor.writeheader()
    escritor.writerows(personas)
```

---

## JSON

```python
import json

datos = {
    "nombre": "Ana",
    "edad": 28,
    "hobbies": ["leer", "correr"],
}

# Escribir JSON a fichero
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)

# Leer JSON desde fichero
with open("datos.json", "r", encoding="utf-8") as f:
    cargado = json.load(f)

print(cargado["nombre"])   # "Ana"

# Convertir entre dict y string JSON (sin fichero)
texto_json = json.dumps(datos)         # dict → string
datos_dict = json.loads(texto_json)    # string → dict
```

---

## Comprobar si un fichero existe

```python
from pathlib import Path

ruta = Path("datos.txt")
if ruta.exists():
    print("El fichero existe")

# Otras utilidades útiles de pathlib
Path("datos.txt").stem        # "datos"      — nombre sin extensión
Path("datos.txt").suffix      # ".txt"       — extensión
Path("datos.txt").parent      # Path(".")    — directorio padre
Path("carpeta") / "sub" / "fichero.txt"  # construir rutas multiplataforma
```

> Usa siempre `encoding="utf-8"` al abrir ficheros de texto para evitar sorpresas en Windows.
