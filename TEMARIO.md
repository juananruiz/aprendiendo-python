# Temario del curso

Este curso se organiza en **cuatro pistas** que responden a cuatro objetivos
(ver la filosofía completa en el [README](README.md)): implementar algoritmos
clásicos, automatizar tareas cotidianas, construir una base sólida de Python
idiomático, y entrenar deliberadamente el pensamiento funcional.

Cada lección es un HTML autocontenido en `lecciones/` con teoría completa, y
casi todas llevan un esqueleto de ejercicio en `ejercicios/` para teclear —
muchos con `assert`s de autoverificación: si pasan, el tema está superado.

> **Para tu seguimiento**: copia este temario a un fichero privado (p. ej.
> `personal/PROGRESO.md`, ignorado por git) y marca ahí tus hitos con `[x]`.

---

## Pista 1 — Algoritmos

> Objetivo: *implementar y entender algoritmos clásicos siguiendo el libro
> "Comprender los algoritmos" de Aditya Y. Bhargava*.

### El libro, capítulo a capítulo

- Introducción a Big O — la búsqueda binaria como primer ejemplo (`algoritmos/busqueda_binaria_01.py`, `busqueda_binaria_02.py`)
- Notación Big O a fondo: O(1), O(log n), O(n), O(n log n), O(n²) *(pendiente)*
- Selection sort (`algoritmos/orden_seleccion_01.py`)
- Recursión: caso base, caso recursivo, la pila de llamadas (`algoritmos/factorial_recursivo.py`, `algoritmos/cuadrar_parcela.py`)
- Quicksort: divide y vencerás, partición — `lecciones/algoritmos/020-quicksort.html`, `ejercicios/algoritmos/020-quicksort.py`
- Hash tables: cómo funciona un `dict` por dentro, colisiones *(pendiente)*
- Grafos y búsqueda en anchura (BFS) *(pendiente)*
- Algoritmo de Dijkstra (caminos más cortos con peso) *(pendiente)*
- Algoritmos voraces (greedy) y una primera idea de problemas NP-completos *(pendiente)*
- Programación dinámica *(pendiente)*
- K-nearest neighbors (KNN) *(pendiente)*
- *(opcional)* Otros algoritmos del libro: árboles, MapReduce, filtros de Bloom

### Otros algoritmos clásicos (no vienen del libro, pero consolidan lo mismo)

- Búsqueda lineal
- Ordenamiento burbuja (`algoritmos/orden_burbuja.py`)
- Ordenamiento por inserción *(pendiente)*
- Cuadrado mágico — verificación (`algoritmos/cuadrado_magico.py`)
- Diferencia diagonal en matrices (`ejercicios/matematicas/ejercicio-diferencia-diagonal.py`)
- Comparar algoritmos midiendo tiempo real con el módulo `time` *(pendiente)*

### Proyecto insignia — el algoritmo del amor (Gale-Shapley)

> El caso de estudio que vertebra el curso: la asignación de destinos en un
> proceso selectivo (candidatos con puntuaciones, plazas con preferencias),
> resuelta con el algoritmo de Gale-Shapley (1962). No viene del libro de
> Bhargava, pero es el mismo tipo de ejercicio — con la ventaja de ser un
> problema real que cualquiera puede reconocer.

#### Rama A — Conceptos previos y aproximación

- Diccionarios para modelar preferencias — `lecciones/matching/001-preferencias-con-diccionarios.html`, `ejercicios/matching/001-generar-ranking.py`, `ejercicios/matching/001a-diccionarios.py`
- Ordenar listas con `sorted()` y `key=` con funciones lambda — `lecciones/matching/002-ordenacion-con-key.html`, `ejercicios/matching/002-ordenar-con-key.py`
- `collections.deque`: cola eficiente para participantes aún no asignados — `lecciones/matching/003-deque-y-colas.html`, `ejercicios/matching/003-colas-con-deque.py`
- Estabilidad y pares bloqueantes — `lecciones/matching/004-estabilidad-y-pares-bloqueantes.html`, `ejercicios/matching/004-detectar-par-bloqueante.py`

#### Rama B — Gale-Shapley en detalle

> Requiere Rama A completa. No se pasa de un tema al siguiente sin haber
> cerrado el anterior. Todas las lecciones están enlazadas entre sí y
> accesibles desde [`lecciones/index.html`](lecciones/index.html).

- **005 — El problema de los matrimonios estables** — `lecciones/matching/005-el-problema-de-los-matrimonios-estables.html` · `ejercicios/matching/005-fuerza-bruta-matchings.py`
  La historia real (Gale, Shapley, el Nobel de 2012 y el NRMP), el planteamiento formal, y por qué la fuerza bruta de N! no sirve
- **006 — El cortejo, ronda a ronda** — `lecciones/matching/006-el-cortejo-ronda-a-ronda.html` · `ejercicios/matching/006-una-ronda-de-cortejo.py`
  Las reglas exactas del algoritmo y un ejemplo 4×4 trazado a mano
- **007 — Por qué funciona** — `lecciones/matching/007-por-que-funciona.html` · `ejercicios/matching/007-verificar-teoremas.py`
  Las cuatro garantías: terminación (N²), completitud, estabilidad y optimalidad del lado que propone
- **008 — Implementación guiada** *(pendiente)*
  Traducir las reglas a código completo con `deque` + diccionarios, y verificar la estabilidad del resultado
- **009 — Variantes reales** *(pendiente)*
  Conjuntos de distinto tamaño, plazas múltiples, preferencias desde puntuaciones, notas de corte y empates
- **010 — Algoritmos relacionados** *(pendiente)*
  Serial dictatorship, algoritmo húngaro, Top Trading Cycles, Stable Roommates
- **Ejercicio de consolidación final** *(pendiente)*
  Simular la asignación completa de un proceso selectivo realista y comparar Gale-Shapley con serial dictatorship y el húngaro

---

## Pista 2 — Automatización

> Objetivo: *automatizar tareas del día a día* — Python como herramienta de
> propósito general, no como framework web.

*(Esta pista está definida pero aún sin lecciones — es la principal laguna
del curso. Los temas marcados son el plan de trabajo.)*

### Ficheros y datos
- Leer y escribir ficheros de texto (`open`, `with`) *(pendiente)*
- CSV con el módulo `csv` · JSON con el módulo `json` *(pendiente)*
- `os` y `pathlib`: recorrer, mover y renombrar ficheros/carpetas *(pendiente)*
- `shutil`: copiar, mover, comprimir *(pendiente)*

### Conectar con el exterior (sin construir una web)
- Consumir APIs externas con `httpx` *(pendiente)*
- Variables de entorno con `python-dotenv` — nunca credenciales en código *(pendiente)*
- Scraping con `BeautifulSoup` o `playwright` — extraer datos, no servirlos *(pendiente)*

### Programar y empaquetar tareas
- CLI con `argparse` o `typer` *(pendiente)*
- Tareas programadas: módulo `schedule` o cron *(pendiente)*
- Bot de Telegram o Discord para una automatización concreta *(pendiente)*

### Persistencia ligera
- SQLite básico con SQLAlchemy (`database.py`)
- Consultas SQL crudas con `sqlite3` *(pendiente)*

### Análisis de datos ligero
- Matrices con listas anidadas (`ejercicios/matematicas/matrice.py`)
- SymPy: cálculo simbólico (`ejercicios/matematicas/derivada.py`, `ejercicios/matematicas/ecuaciones_lineales.py`)
- NumPy, Pandas, Matplotlib *(pendientes)*
- Proyecto: analizar un dataset real que te sea útil *(pendiente)*

### Proyecto insignia
- Elige una tarea repetitiva de tu día a día y automatízala de principio a fin: ficheros o API + procesado + programación de la tarea + manejo de errores

---

## Pista 3 — Fundamentos y base sólida

> Objetivo: *escribir Python idiomático sin pensar en la sintaxis* y *tener
> criterio para elegir la estructura de datos correcta*. Esta pista no tiene
> un "final": es la base de las otras dos, y se revisita cuando hace falta.

### Variables y tipos básicos
- Tipos, operaciones, conversiones, f-strings — ver `REFERENCIA_PYTHON/01_tipos_y_variables.md` y `02_strings.md`
- Mutable vs inmutable, `is` vs `==`

### Control de flujo
- `if/elif/else`, `for` con `range()`
- El bucle `while` a fondo (contador, centinela, bandera, `while True` + `break`, `while/else`, bucles infinitos) — `lecciones/fundamentos/030-el-bucle-while.html`, `ejercicios/fundamentos/030-el-bucle-while.py`
- Slicing, `enumerate()`, `for/else`, `break`/`continue` — `lecciones/fundamentos/0001-slicing-enumerate-y-control-de-bucles.html`

### Funciones
- `def`, parámetros, retorno, recursión básica — ver Pista 1
- Parámetros por defecto, keyword arguments, scope *(pendiente)*

### Manejo de errores
- `try/except/finally`, excepciones comunes, `raise` *(pendiente — la referencia `REFERENCIA_PYTHON/07_errores_y_excepciones.md` cubre la consulta rápida)*

### Estructuras de datos
- Listas, tuplas, diccionarios, conjuntos: cuándo usar cada una *(lección pendiente; referencia en `REFERENCIA_PYTHON/03_listas.md` y `04_diccionarios_y_conjuntos.md`, cheatsheet visual en `REFERENCIA_PYTHON/colecciones_cheatsheet.html`)*
- Ejercicios de consolidación *(pendientes)*: agenda de contactos con diccionarios; inventario con listas de diccionarios

### Módulos y entorno
- Imports, `venv`, `pip` y `requirements.txt`, `__name__ == "__main__"` — ver `REFERENCIA_PYTHON/09_modulos.md`

### Programación orientada a objetos *(pendiente)*
- Clases, `__init__`, métodos, `__str__`/`__repr__`, herencia, `@property`/`@staticmethod`, y cuándo NO usar clases (YAGNI)
- Ejercicio de consolidación: biblioteca con `Libro`, `Usuario` y `Biblioteca`

### Python idiomático (lo que no es ni POO ni funcional)
- Unpacking, `enumerate()`/`zip()`, context managers *(pendiente)*

### Testing *(pendiente)*
- `pytest`, Arrange-Act-Assert, fixtures, mocking, cobertura — y añadir tests a los scripts del curso

---

## Pista 4 — Programación funcional

> Objetivo: *entrenar deliberadamente el pensamiento funcional*. Si vienes de
> un lenguaje donde trabajas en modo OOP (PHP, Java, C#...), esta pista es
> intencionadamente el paradigma contrario: no es indispensable para Python,
> es un cambio de aires para ejercitar otro músculo mental.

> **Pista completa.** Se recorre en orden — cada lección se apoya en la
> anterior. Cada ejercicio trae `assert`s: si pasan, el tema está superado.

- **011 — Funciones puras e inmutabilidad** — `lecciones/funcional/011-funciones-puras-e-inmutabilidad.html` · `ejercicios/funcional/011-funciones-puras.py`
  Determinismo, efectos secundarios, el gotcha del argumento por defecto mutable, y el patrón "núcleo funcional, cáscara imperativa"
- **012 — Funciones de primera clase y composición** — `lecciones/funcional/012-funciones-de-primera-clase-y-composicion.html` · `ejercicios/funcional/012-orden-superior-y-composicion.py`
  Funciones como valores, closures (y su gotcha en bucles), orden superior y composición
- **013 — `lambda`, `map`, `filter` y comprehensions** — `lecciones/funcional/013-lambda-map-filter-y-comprehensions.html` · `ejercicios/funcional/013-map-filter-comprehensions.py`
- **014 — Generadores y evaluación perezosa** — `lecciones/funcional/014-generadores-y-evaluacion-perezosa.html` · `ejercicios/funcional/014-generadores.py`
- **015 — El módulo `functools`** — `lecciones/funcional/015-functools.html` · `ejercicios/funcional/015-functools.py`
- **016 — El módulo `itertools`** — `lecciones/funcional/016-itertools.html` · `ejercicios/funcional/016-itertools.py`
- **017 — Decoradores de propósito general** — `lecciones/funcional/017-decoradores.html` · `ejercicios/funcional/017-decoradores.py`
- **018 — Proyecto: contraste imperativo vs. funcional** — `ejercicios/funcional/018-imperativo-vs-funcional.py`
  Reescribir un script imperativo en estilo funcional puro, montar un pipeline sin variables mutables, y una reflexión final: el objetivo es criterio, no dogma

---

## Extras fuera de temario

El repositorio incluye además algunos scripts exploratorios que no forman
parte de las pistas (UI con Flet en `counter.py`, mini-APIs con Flask y
FastAPI en `flask_demo.py` y `fastapi_ia.py`, gráficos con matplotlib en
`sol_tierra.py`). Quedan como ejemplos de hasta dónde puede llegar Python,
pero el desarrollo web queda deliberadamente fuera de los objetivos del curso.
