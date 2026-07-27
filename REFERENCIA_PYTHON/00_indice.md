# Referencia Python — Índice

Consultas rápidas sin necesidad de buscar en Google.

| Archivo | Contenido |
|---------|-----------|
| [01_tipos_y_variables.md](01_tipos_y_variables.md) | Tipos básicos, conversiones, operadores |
| [02_strings.md](02_strings.md) | Métodos de strings, f-strings, slicing |
| [03_listas.md](03_listas.md) | Listas, list comprehensions, métodos |
| [04_diccionarios_y_conjuntos.md](04_diccionarios_y_conjuntos.md) | Dicts, sets, tuplas |
| [05_control_de_flujo.md](05_control_de_flujo.md) | if/elif/else, for, while, break, continue |
| [06_funciones.md](06_funciones.md) | def, parámetros, scope, lambda |
| [07_errores_y_excepciones.md](07_errores_y_excepciones.md) | try/except, raise, excepciones comunes |
| [08_ficheros.md](08_ficheros.md) | Leer/escribir txt, CSV, JSON |
| [09_modulos.md](09_modulos.md) | import, módulos útiles de la stdlib |
| [10_clases.md](10_clases.md) | POO básica: class, __init__, herencia |

> Estos archivos son una referencia viva. Añade ejemplos tuyos cuando los necesites.

---

## Visto en el laboratorio

Cada tema de la referencia no es abstracto: ya lo has usado en tus propios
scripts. Esta tabla enlaza la teoría con el código real donde aparece, para
que puedas ir del concepto al ejemplo vivido (y al revés).

| Tema | Dónde lo has usado |
|------|--------------------|
| [01 Tipos y variables](01_tipos_y_variables.md) | [`babylonian_square_root.py`](../algoritmos/babylonian_square_root.py) usa `math.isclose` para comparar `float` (justo el error frecuente de la precisión); [`cuadrar_parcela.py`](../algoritmos/cuadrar_parcela.py) intercambia con `x, y = y, x` |
| [02 Strings](02_strings.md) | [`busqueda_binaria_02.py`](../algoritmos/busqueda_binaria_02.py) construye el prompt con una f-string |
| [03 Listas](03_listas.md) | [`orden_burbuja.py`](../algoritmos/orden_burbuja.py), [`orden_seleccion_01.py`](../algoritmos/orden_seleccion_01.py) (con `pop()`), [`busqueda_binaria_01.py`](../algoritmos/busqueda_binaria_01.py) (`random.sample` + `sort()`) |
| [04 Diccionarios y conjuntos](04_diccionarios_y_conjuntos.md) | [`ejercicios/001a-diccionarios.py`](../ejercicios/001a-diccionarios.py) y toda la Rama A de matching (preferencias como dicts) |
| [05 Control de flujo](05_control_de_flujo.md) | [`busqueda_binaria_02.py`](../algoritmos/busqueda_binaria_02.py) (`while` + `if/elif` + `break`), [`orden_burbuja.py`](../algoritmos/orden_burbuja.py) (`while` con bandera) |
| [06 Funciones](06_funciones.md) | [`factorial_recursivo.py`](../algoritmos/factorial_recursivo.py) y [`cuadrar_parcela.py`](../algoritmos/cuadrar_parcela.py) (recursión), [`cuadrado_magico.py`](../algoritmos/cuadrado_magico.py) |
| [07 Errores y excepciones](07_errores_y_excepciones.md) | [`babylonian_square_root.py`](../algoritmos/babylonian_square_root.py) lanza `ValueError` con `raise` |
| [08 Ficheros](08_ficheros.md) | *(pendiente — aún no hay un script del laboratorio que lea/escriba ficheros; buen candidato para el próximo ejercicio)* |
| [09 Módulos](09_modulos.md) | `import random` en las búsquedas, `import math` en [`babylonian_square_root.py`](../algoritmos/babylonian_square_root.py), `matplotlib` en [`sol_tierra.py`](../sol_tierra.py) |
| [10 Clases](10_clases.md) | [`database.py`](../database.py) define `class PeticionDB(Base)` (modelo SQLAlchemy) |
