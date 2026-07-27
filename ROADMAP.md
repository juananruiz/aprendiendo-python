# Roadmap de aprendizaje Python

Marca cada hito con `[x]` cuando lo hayas superado.

> **Reestructurado el 21/07/2026** para reflejar los 3 objetivos de
> [MISSION.md](MISSION.md), en vez de un temario genérico de 12 niveles.
> Antes había un **Nivel 9 (Flask/FastAPI)** activo que contradecía tu
> no-objetivo de no ser desarrollador web en Python — se ha retirado. Lo que
> sí era reutilizable de ese nivel (consumir APIs externas, JSON, variables
> de entorno) se reubica en la Pista 2, porque eso es automatización, no
> desarrollo web. El resto de niveles se han fusionado en 3 pistas; nada de
> lo marcado `[x]` se ha perdido.

---

## Pista 1 — Algoritmos

> Objetivo de la MISSION: *"Implementar y entender algoritmos clásicos
> siguiendo el libro 'Comprender los algoritmos' de Aditya Y. Bhargava"*.

### El libro, capítulo a capítulo

- [x] Introducción a Big O — la búsqueda binaria como primer ejemplo (`algoritmos/busqueda_binaria_01.py`, `busqueda_binaria_02.py`)
- [ ] Notación Big O a fondo: O(1), O(log n), O(n), O(n log n), O(n²)
- [x] Selection sort (`algoritmos/orden_seleccion_01.py`)
- [x] Recursión: caso base, caso recursivo, la pila de llamadas (`algoritmos/factorial_recursivo.py`, `algoritmos/cuadrar_parcela.py`)
- [ ] Quicksort: divide y vencerás, partición — `lecciones/020-quicksort.html`, `ejercicios/020-quicksort.py`
- [ ] Hash tables: cómo funciona un `dict` por dentro, colisiones
- [ ] Grafos y búsqueda en anchura (BFS)
- [ ] Algoritmo de Dijkstra (caminos más cortos con peso)
- [ ] Algoritmos voraces (greedy) y una primera idea de problemas NP-completos
- [ ] Programación dinámica
- [ ] K-nearest neighbors (KNN)
- [ ] *(opcional, si sobra tiempo)* Otros algoritmos del libro: árboles, MapReduce, filtros de Bloom

### Otros algoritmos ya trabajados (no vienen del libro, pero consolidan lo mismo)

- [x] Búsqueda lineal
- [x] Ordenamiento burbuja (`algoritmos/orden_burbuja.py`)
- [ ] Ordenamiento por inserción
- [ ] Cuadrado mágico — verificación (`algoritmos/cuadrado_magico.py`)
- [ ] Diferencia diagonal en matrices (`matematicas/ejercicio-diferencia-diagonal.py`, `diferencia-diagonal.py`)
- [ ] Comparar algoritmos midiendo tiempo real con el módulo `time`

### Proyecto insignia — Rama A y B: el algoritmo del amor

> Esta es la aplicación real de "implementar y entender un algoritmo desde
> cero": el problema de asignación de plazas que usas en tu trabajo,
> resuelto con Gale-Shapley (1962). No viene del libro de Bhargava, pero es
> el mismo tipo de ejercicio que persigue el objetivo de la Pista 1 — y
> tiene la ventaja de ser un problema que ya te importa de verdad.

#### Rama A — Conceptos previos y aproximación

- [ ] Diccionarios para modelar preferencias (clave = participante, valor = lista de destinos ordenados) — `lecciones/001-preferencias-con-diccionarios.html`, `ejercicios/001-generar-ranking.py`, `ejercicios/001a-diccionarios.py`
- [ ] Ordenar listas con `sorted()` y `key=` con funciones lambda — `lecciones/002-ordenacion-con-key.html`, `ejercicios/002-ordenar-con-key.py`
- [ ] `collections.deque`: cola eficiente para participantes aún no asignados — `lecciones/003-deque-y-colas.html`, `ejercicios/003-colas-con-deque.py`
- [ ] Comprensión de estabilidad: ¿qué significa que un matching sea estable? ¿qué es un *par bloqueante*? — `lecciones/004-estabilidad-y-pares-bloqueantes.html`, `ejercicios/004-detectar-par-bloqueante.py`

#### Rama B — El algoritmo del amor (Gale-Shapley en detalle)

> Requiere Rama A completa. Cada lección es un HTML con teoría completa y
> un ejercicio práctico en Python para teclear tú. No se pasa de un tema al
> siguiente sin haber cerrado el anterior. Todas las lecciones (Rama A y B)
> están enlazadas entre sí y accesibles desde
> [`lecciones/index.html`](lecciones/index.html).

**005 — El problema de los matrimonios estables**
`lecciones/005-el-problema-de-los-matrimonios-estables.html` · `ejercicios/005-fuerza-bruta-matchings.py`
- [ ] La historia real: Gale y Shapley (1962), el Nobel de Economía 2012, y el NRMP (asignación de médicos residentes en EEUU)
- [ ] Planteamiento formal completo: dos conjuntos del mismo tamaño, preferencias completas y sin empates
- [ ] Qué es exactamente un *matching* (repaso formal, sin dar nada por supuesto)
- [ ] Por qué la fuerza bruta no sirve: la combinatoria de N! emparejamientos posibles
- [ ] El teorema de Gale-Shapley (enunciado, sin demostrar todavía): siempre existe un matching estable

**006 — El cortejo, ronda a ronda**
`lecciones/006-el-cortejo-ronda-a-ronda.html` · `ejercicios/006-una-ronda-de-cortejo.py`
- [ ] La metáfora del cortejo: propuestas, aceptación provisional, rechazo
- [ ] Las reglas exactas del algoritmo, una a una
- [ ] Ejemplo completo de 4×4 trazado a mano, ronda a ronda, con tabla de estados
- [ ] Por qué nadie propone dos veces a la misma persona

**007 — Por qué funciona**
`lecciones/007-por-que-funciona.html` · `ejercicios/007-verificar-teoremas.py`
- [ ] ¿Por qué el algoritmo siempre termina? (cota de N² propuestas como máximo)
- [ ] ¿Por qué el resultado es siempre un matching completo?
- [ ] ¿Por qué el resultado es siempre estable? (demostración por contradicción, intuitiva)
- [ ] Optimalidad: el lado que propone obtiene su mejor matching estable posible; el lado que recibe, el peor

**008 — Implementación guiada** *(pendiente)*
- [ ] Traducir las reglas de la lección 006 a código, línea a línea
- [ ] Implementación completa con `deque` + diccionarios de preferencias
- [ ] Verificar estabilidad del resultado con la función de la lección 004

**009 — Variantes reales** *(pendiente)*
- [ ] Conjuntos de distinto tamaño (hospital/residentes, plazas múltiples)
- [ ] Preferencias a partir de puntuaciones numéricas en vez de rankings declarados
- [ ] Notas de corte y empates

**010 — Algoritmos relacionados** *(pendiente)*
- [ ] **Serial dictatorship**: el que más puntuación tiene elige primero. Comparar con Gale-Shapley
- [ ] **Hungarian algorithm**: asignación óptima por coste total, no por estabilidad
- [ ] **Top Trading Cycles (TTC)**: permutas entre ya asignados
- [ ] **Stable Roommates**: un único conjunto, sin garantía de estabilidad

**Ejercicio de consolidación final**
- [ ] Simular la asignación de destinos de tu proceso selectivo real: candidatos con puntuaciones, plazas con perfiles, preferencias automáticas, Gale-Shapley + verificación de estabilidad
- [ ] Comparar el resultado con serial dictatorship y Hungarian: ¿quién sale beneficiado en cada caso?

---

## Pista 2 — Automatización

> Objetivo de la MISSION: *"Automatizar tareas del día a día (fuera del
> desarrollo web, que ya cubro con PHP/React)"*.

### Ficheros y datos

- [ ] Leer y escribir ficheros de texto (`open`, `with`)
- [ ] Leer y escribir CSV con el módulo `csv`
- [ ] Leer y escribir JSON con el módulo `json`
- [ ] `os` y `pathlib`: recorrer, mover y renombrar ficheros/carpetas
- [ ] `shutil`: copiar, mover, comprimir

### Conectar con el exterior (sin construir una web)

- [ ] Consumir APIs externas con `httpx` (petición, respuesta, manejar JSON)
- [ ] Variables de entorno con `python-dotenv` (nunca credenciales en código)
- [ ] Scraper web con `BeautifulSoup` o `playwright` — extraer datos, no servirlos

### Programar y empaquetar tareas

- [ ] CLI tool con `argparse` o `typer`
- [ ] Programar tareas repetidas: módulo `schedule` o cron del sistema
- [ ] Bot de Telegram o Discord para una automatización personal concreta

### Persistencia ligera para tus scripts

- [x] SQLite básico con SQLAlchemy (`database.py`)
- [ ] Consultas SQL crudas con `sqlite3`
- [ ] *(opcional, baja prioridad — más orientado a backends web que a scripts)* ORM completo con relaciones, Alembic, PostgreSQL

### Análisis de datos ligero

> Parte del objetivo #3 de la MISSION ("base sólida para incursionar en
> análisis de datos"), aplicado aquí como herramienta de automatización, no
> como especialización en ciencia de datos (no-objetivo explícito).

- [x] Matrices con listas anidadas, manual (`matematicas/matrice.py`)
- [x] SymPy: cálculo simbólico — derivadas, ecuaciones lineales (`derivada.py`, `matematicas/ecuaciones_lineales.py`)
- [ ] NumPy: arrays, operaciones vectorizadas
- [ ] Pandas: DataFrames, leer CSV, filtrar, agrupar
- [ ] Matplotlib: gráficas de línea, barras, histograma
- [ ] Proyecto: analizar un dataset real que te sea útil (no de juguete)

### Proyecto insignia — automatiza algo tuyo de verdad

- [ ] **Elige una tarea repetitiva de tu día a día** (no de desarrollo web) y automatízala de principio a fin: ficheros o API + procesado + programación de la tarea + manejo de errores

---

## Pista 3 — Fundamentos y base sólida

> Objetivo de la MISSION: *"Escribir Python idiomático sin pensar en la
> sintaxis"* y *"tener criterio para elegir la estructura de datos
> correcta"*. Esta pista no tiene un "final": es la base sobre la que
> se apoyan las otras dos, y se revisita cuando haga falta.

### Variables y tipos básicos

- [x] Entender tipos: `int`, `float`, `str`, `bool`
- [x] Operaciones aritméticas y de comparación
- [ ] Conversión de tipos (`int()`, `str()`, `float()`)
- [x] f-strings para formatear texto
- [ ] Mutable vs inmutable, `is` vs `==` (ver `REFERENCIA_PYTHON/01_tipos_y_variables.md`)

### Control de flujo

- [x] `if / elif / else`
- [x] Bucle `while`
- [x] Bucle `for` con `range()`
- [ ] `break`, `continue`, `pass` — `lecciones/030-el-bucle-while.html`, `ejercicios/030-el-bucle-while.py`
- [ ] `while / else` — mismos ficheros que arriba
- [ ] `for / else` — ver `lecciones/0001-slicing-enumerate-y-control-de-bucles.html`

### Funciones

- [x] Definir funciones con `def`
- [x] Parámetros y valor de retorno
- [ ] Parámetros por defecto y keyword arguments
- [ ] Scope: variables locales vs globales
- [x] Funciones que llaman a otras funciones (recursión básica) — ver Pista 1

### Manejo de errores

- [ ] `try / except / finally`
- [ ] Tipos de excepciones comunes (`ValueError`, `TypeError`, `KeyError`...)
- [ ] Lanzar excepciones con `raise`

### Estructuras de datos

- [x] Listas: crear, indexar, recorrer, `append()`, `sort()`, `len()`
- [ ] Slicing (`lista[1:4]`, `lista[::-1]`) — ver `lecciones/0001-slicing-enumerate-y-control-de-bucles.html`
- [ ] Listas anidadas (matrices 2D)
- [ ] Tuplas: cuándo usarlas en vez de listas
- [ ] Diccionarios: crear, acceder, iterar, anidados
- [ ] Conjuntos (`set`): unión, intersección, diferencia
- [ ] Cuándo usar cada estructura y por qué

**Ejercicio de consolidación**
- [ ] Implementar una agenda de contactos con diccionarios
- [ ] Implementar un inventario de productos con listas de diccionarios

### Strings

- [ ] Métodos clave: `split()`, `strip()`, `replace()`, `upper()`, `lower()`
- [ ] Indexado y slicing de strings
- [ ] `join()` para construir strings desde listas

### Módulos y entorno

- [x] Importar módulos de la librería estándar (`random`, `math`)
- [x] Usar `venv` para aislar dependencias
- [ ] Crear tus propios módulos (ficheros `.py` que importas)
- [ ] Gestionar paquetes con `pip` y `requirements.txt`
- [ ] Entender `__name__ == "__main__"`

### Programación orientada a objetos (POO)

- [ ] Qué es una clase y para qué sirve
- [ ] `__init__`, atributos de instancia
- [ ] Métodos de instancia
- [ ] `__str__` y `__repr__`
- [ ] Herencia básica
- [ ] Sobreescribir métodos
- [ ] `@property` y `@staticmethod` (decoradores propios de clases)
- [ ] Cuándo NO usar clases (YAGNI)

**Ejercicio de consolidación**
- [ ] Modelar una biblioteca con clases `Libro`, `Usuario` y `Biblioteca`

### Python idiomático (lo que no es ni POO ni funcional)

- [ ] Unpacking: `a, b = (1, 2)`
- [ ] `enumerate()` y `zip()`
- [ ] Context managers (`with`) y crear los tuyos

> El resto de "Python idiomático" — lambda, comprehensions, generadores,
> `map`/`filter`, decoradores de propósito general — vive ahora en la
> **Pista 4**, porque es precisamente el terreno funcional que quieres
> entrenar a propósito.

### Testing

> No es una casilla que "se termina" antes de seguir — se practica sobre
> la marcha en cuanto un script deja de ser de un solo uso.

- [ ] `pytest` básico: escribir y ejecutar tests
- [ ] Patrón Arrange-Act-Assert
- [ ] Tests con fixtures
- [ ] Mocking con `unittest.mock`
- [ ] Cobertura con `pytest-cov`
- [ ] Añadir tests a alguno de los scripts ya escritos

### Proyectos ya explorados (curiosidad, no objetivo activo)

> Estos no son parte de ninguna de las 3 pistas de la MISSION, pero ya los
> hiciste y no hay razón para borrarlos — quedan como referencia.

- [x] Chatbot con Google AI (`ChatbotGoogleAI.py`)
- [x] Chatbot con HuggingFace (`ChatbotHugginFace.py`)
- [x] UI con Flet — contador (`counter.py`)
- [x] Flask básico y FastAPI básico (`flask_demo.py`, `fastapi_ia.py`, `templates/index.html`) — explorados, pero **fuera de la MISSION** (no-objetivo explícito de no ser dev web en Python); no se retoman salvo que cambie el objetivo

---

## Pista 4 — Programación funcional

> Objetivo de la MISSION: *"Pensar en programación funcional — un cambio de
> aires deliberado"*. En PHP trabajas en modo OOP; esta pista es
> intencionadamente el paradigma contrario. No es indispensable para
> Python, es una elección tuya para ejercitar otro músculo mental.

> **Material disponible (21/07/2026).** La pista completa está escrita:
> lecciones **011–017** en `lecciones/` (HTML, mismo formato que la rama de
> matching) y sus esqueletos de ejercicio en `ejercicios/`. Cada ejercicio
> trae `assert`s al final: si pasan, el tema está superado. Se recorren en
> orden — cada lección se apoya en la anterior.

### Conceptos base

**011 — Funciones puras e inmutabilidad**
`lecciones/011-funciones-puras-e-inmutabilidad.html` · `ejercicios/011-funciones-puras.py`
- [ ] Funciones puras: sin efectos secundarios, mismo input → mismo output
- [ ] Inmutabilidad: por qué preferir crear datos nuevos a mutar los existentes (contraste directo con el estado mutable de los objetos en OOP)
- [ ] El gotcha del argumento por defecto mutable
- [ ] Patrón "núcleo funcional, cáscara imperativa"

**012 — Funciones de primera clase y composición**
`lecciones/012-funciones-de-primera-clase-y-composicion.html` · `ejercicios/012-orden-superior-y-composicion.py`
- [ ] Funciones de primera clase: pasar funciones como argumentos, devolverlas como resultado
- [ ] Closures: qué capturan y el gotcha del closure en un bucle
- [ ] Funciones de orden superior y composición de funciones
- [ ] Recursión como alternativa a los bucles — ya cubierta en la Pista 1 (`algoritmos/factorial_recursivo.py`, `algoritmos/cuadrar_parcela.py`), no se repite aquí

### El kit de herramientas de Python

**013 — `lambda`, `map`, `filter` y comprehensions**
`lecciones/013-lambda-map-filter-y-comprehensions.html` · `ejercicios/013-map-filter-comprehensions.py`
- [ ] Funciones lambda
- [ ] `map()` y `filter()` explícitos (antes de pasar a comprehensions)
- [ ] List/dict/set comprehensions como "azúcar" sobre `map`/`filter`
- [ ] `if` como filtro vs. `if` como expresión ternaria

**014 — Generadores y evaluación perezosa**
`lecciones/014-generadores-y-evaluacion-perezosa.html` · `ejercicios/014-generadores.py`
- [ ] Generadores y `yield` — evaluación perezosa
- [ ] Secuencias infinitas sin agotar la memoria
- [ ] Pipelines de varias etapas sobre ficheros grandes
- [ ] El agotamiento de los generadores y `yield from`

**015 — El módulo `functools`**
`lecciones/015-functools.html` · `ejercicios/015-functools.py`
- [ ] Módulo `functools`: `reduce`, `partial`, `lru_cache`, `wraps`

**016 — El módulo `itertools`**
`lecciones/016-itertools.html` · `ejercicios/016-itertools.py`
- [ ] Módulo `itertools`: `chain`, `islice`, `groupby`, `product`, `takewhile`/`dropwhile`
- [ ] La regla de oro: `sorted()` antes de `groupby()`

**017 — Decoradores de propósito general**
`lecciones/017-decoradores.html` · `ejercicios/017-decoradores.py`
- [ ] Decoradores de propósito general (más allá de `@property`/`@staticmethod`, que son de la Pista 3)
- [ ] Decoradores con parámetros (los tres niveles de anidamiento)
- [ ] Apilar decoradores y por qué importa el orden

### Proyecto insignia — contraste imperativo vs. funcional

`ejercicios/018-imperativo-vs-funcional.py`
- [ ] Reescribe un script ya hecho en estilo imperativo (por ejemplo `algoritmos/orden_burbuja.py` o `algoritmos/busqueda_binaria_01.py`) en estilo funcional puro: sin bucles `for`/`while` explícitos, encadenando `map`/`filter`/`reduce`/comprehensions
- [ ] Monta un pipeline de procesamiento de datos (puede reutilizar un CSV/JSON de la Pista 2) usando solo funciones encadenadas, sin variables mutables intermedias
- [ ] Reflexión escrita: ¿en qué casos el estilo funcional salió más claro que el imperativo, y en cuáles fue forzar la nota? (el objetivo es criterio, no dogma)

---

## Notas y reflexiones

- Empecé con algoritmos clásicos antes de entrar en POO — buena decisión para asentar lógica pura.
- He probado Flask, FastAPI y Flet antes de dominar los fundamentos — está bien para motivarse, pero conviene volver y consolidar Pista 3 antes de retomar proyectos grandes.
- `orden_seleccion_01.py` (02/07/2026) implementa **ordenamiento por selección**: en cada pasada busca el mínimo del subconjunto no ordenado y lo extrae con `pop()`. Correcto, aunque el `pop()` en posición intermedia añade un coste O(n) extra frente a la versión clásica por intercambio in-place. Complejidad total: O(n²) en ambos casos.
- **21/07/2026** — Reestructuré el roadmap de 12 niveles genéricos a 3 pistas (Algoritmos / Automatización / Fundamentos) para que reflejen directamente los objetivos de MISSION.md. Retiré Flask/FastAPI como objetivo activo por contradecir el no-objetivo de desarrollo web; lo que era reutilizable (APIs externas, JSON, dotenv) se movió a Automatización.
- **21/07/2026** — Escrita la Pista 4 completa: lecciones 011–017 en `lecciones/` + esqueletos 011–017 y el capstone 018 en `ejercicios/`. Los ejercicios llevan `assert`s de autoverificación; ninguno viene resuelto. Numeración a partir de 011 para no pisar los huecos 008–010, reservados a la rama Gale-Shapley.
- **21/07/2026** — Añadida Pista 4 (Programación funcional) como 4º objetivo explícito de MISSION.md: contraste deliberado con el estilo OOP de PHP, no una necesidad del lenguaje. Se movieron aquí lambda, comprehensions, generadores, `map`/`filter` y decoradores de propósito general, que antes estaban sueltos en "Python idiomático" (Pista 3); se quedaron en Pista 3 solo `@property`/`@staticmethod` (específicos de POO), unpacking, `enumerate`/`zip` y context managers.
