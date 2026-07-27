# Módulos

## Importar

```python
import math
import math as m        # alias
from math import sqrt   # importar solo lo que necesitas
from math import *      # importa todo — evitar en proyectos grandes

math.sqrt(16)           # 4.0
m.pi                    # 3.141592...
sqrt(25)                # 5.0  (importado directamente)
```

## Crear tu propio módulo

Cualquier fichero `.py` es un módulo. Si tienes `utilidades.py`:

```python
# utilidades.py
def saludar(nombre):
    return f"Hola, {nombre}"

PI = 3.14159
```

Lo importas desde otro fichero en el mismo directorio:

```python
from utilidades import saludar, PI
print(saludar("Ana"))
```

## `__name__ == "__main__"`

```python
# modulo.py
def calcular(x):
    return x * 2

if __name__ == "__main__":
    # Este bloque SOLO se ejecuta si corres el fichero directamente:
    # python modulo.py
    # NO se ejecuta si lo importas desde otro módulo
    print(calcular(5))
```

---

## Otras variables globales de módulo

Además de `__name__`, cada fichero `.py` tiene automáticamente otras variables especiales (los llamados **dunders**, por sus dobles guiones bajos):

```python
__name__      # nombre del módulo: "__main__" si se ejecuta directamente,
              # o el nombre del módulo si se importa (ej: "busqueda_binaria_02")

__file__      # ruta del propio fichero .py
              # ej: "/Users/juananruiz/dev/aprendiendo-python/busqueda_binaria_02.py"

__doc__       # el docstring del módulo (si el fichero empieza con una cadena
              # de documentación en la primera línea)

__package__   # nombre del paquete al que pertenece (None si no está en un paquete)

__loader__    # objeto interno que se usó para cargar el módulo (uso avanzado)

__spec__      # objeto ModuleSpec con metadatos de importación (uso avanzado)

__builtins__  # referencia al módulo de funciones incorporadas (print, len, etc.)
```

### Ejemplo práctico

```python
"""
Este script implementa búsqueda binaria sobre una lista aleatoria.
"""
import random

print(__name__)   # "__main__" al ejecutarlo directamente con python script.py
print(__file__)   # la ruta completa del fichero
print(__doc__)    # el docstring de arriba, porque el fichero lo tiene definido
```

Si el fichero **no** tiene docstring de módulo (no empieza con una cadena de texto entre `"""..."""`), `__doc__` sería `None`.

### Las más útiles en la práctica

De todas ellas, en el día a día solo usarás con frecuencia:

| Variable | Para qué sirve |
|----------|-----------------|
| `__name__` | Distinguir si el fichero se ejecuta directamente o se importa (patrón `if __name__ == "__main__":`) |
| `__file__` | Construir rutas relativas al propio script (ej: `Path(__file__).parent / "datos.csv"`) |
| `__doc__` | Documentación automática, se usa con `help(modulo)` |

El resto (`__package__`, `__loader__`, `__spec__`, `__builtins__`) son mecanismos internos del sistema de importación de Python — casi nunca los tocarás salvo en código muy avanzado (frameworks, plugins dinámicos, etc.).

---

## Módulos útiles de la stdlib

### random

```python
import random

random.randint(1, 10)         # entero entre 1 y 10 (ambos incluidos)
random.random()               # float entre 0.0 y 1.0
random.choice([1, 2, 3])      # elemento aleatorio de la lista
random.sample([1,2,3,4,5], 3) # 3 elementos sin repetición
random.shuffle(lista)          # mezcla la lista en su lugar
```

### math

```python
import math

math.sqrt(9)       # 3.0
math.ceil(3.2)     # 4   — redondea hacia arriba
math.floor(3.9)    # 3   — redondea hacia abajo
math.pow(2, 8)     # 256.0
math.log(100, 10)  # 2.0
math.pi            # 3.14159...
math.e             # 2.71828...
math.inf           # infinito positivo
```

### datetime

```python
from datetime import datetime, date, timedelta

hoy = date.today()               # 2024-06-25
ahora = datetime.now()           # 2024-06-25 14:30:00.123456
ahora.strftime("%d/%m/%Y %H:%M") # "25/06/2024 14:30"

manana = hoy + timedelta(days=1)
diferencia = date(2025, 1, 1) - hoy   # timedelta
diferencia.days                        # número de días
```

### os y pathlib

```python
import os
from pathlib import Path

os.getcwd()                    # directorio actual
os.listdir(".")                # lista ficheros del directorio actual
os.path.exists("fichero.txt") # True/False

# pathlib es más moderna y recomendada
Path.cwd()                     # directorio actual
list(Path(".").iterdir())      # lista ficheros
(Path(".") / "sub" / "f.txt") # construir rutas
```

### sys

```python
import sys

sys.argv           # ["nombre_script.py", "arg1", "arg2", ...]
sys.exit(0)        # termina el programa (0 = éxito, 1 = error)
sys.version        # versión de Python
```

### time

```python
import time

time.time()        # segundos desde epoch (float) — útil para medir tiempos
time.sleep(2)      # pausa 2 segundos

inicio = time.time()
# ... código ...
print(f"Tardó {time.time() - inicio:.3f} segundos")
```

### collections

```python
from collections import Counter, defaultdict, deque

# Counter — cuenta elementos
c = Counter(["a", "b", "a", "c", "a", "b"])
c.most_common(2)   # [("a", 3), ("b", 2)]

# defaultdict — dict que no lanza KeyError
d = defaultdict(list)
d["clave"].append(1)   # no hace falta inicializar la clave

# deque — cola eficiente para añadir/quitar por ambos extremos
cola = deque([1, 2, 3])
cola.appendleft(0)     # [0, 1, 2, 3]
cola.popleft()         # quita y devuelve 0
```
