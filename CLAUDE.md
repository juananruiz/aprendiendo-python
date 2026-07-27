# Aprendiendo Python — Espacio de Aprendizaje

Este directorio es un cuaderno de ejercicios de Python con scripts sueltos, notebooks y pequeños proyectos. No es un proyecto de producción — es un laboratorio.

## Enfoque didáctico

Cuando preguntes sobre Python, prioriza:

1. **Explicar el concepto** antes que dar el código. Si preguntas "cómo hago X", primero responde qué significa X, luego cómo se implementa.
2. **Señalar errores comunes** — off-by-one, mutabilidad, scope, etc. — que son típicos en el nivel del script en cuestión.
3. **Darlo hecho o darlo pensado** según tu objetivo: si es práctica, prefieres pistas; si es参考, dime y te doy la solución completa.
4. **Código en español** cuando sea didáctico (variables, comentarios), en inglés si es para aprender convenciones reales. Sigo tu preferencia.

## Estructura del proyecto

| Directorio | Contenido |
|------------|-----------|
| `algoritmos/` | Algoritmos clásicos (búsqueda, ordenación, numéricos) |
| `lecciones/` | Notas de teoría para cada tema de aprendizaje |
| `ejercicios/` | Ejercicios prácticos para resolver |
| `matematicas/` | Scripts y notebooks matemáticos |
| `templates/` | Templates Flask |
| `learning-records/` | Registros de aprendizaje |
| `meta_python/` | Meta-aprendizaje Python |
| `REFERENCIA_PYTHON/` | Guías de referencia |

## Scripts principales

| Fichero | Tema |
|---------|------|
| `busqueda_binaria.py` | Algoritmos de búsqueda |
| `orden-burbuja.py` | Ordenamiento burbuja |
| `counter.py` | UI con Flet (contador) |
| `database.py` | SQLAlchemy + SQLite |
| `ChatbotGoogleAI.py` | APIs de IA (Google) |
| `ChatbotHugginFace.py` | APIs de IA (HuggingFace) |
| `fastapi_ia.py` | API con FastAPI |
| `flask_demo.py` | Web con Flask |
| `ecuaciones_lineales.py` | Álgebra lineal |
| `derivada.py` | Cálculo simbólico |
| `matrice.py` | Operaciones con matrices |

## Setup técnico

- **Python 3.14.5** — virtualenv en `venv/`
- **Dependencias**: Flet, httpx, SQLAlchemy (instalar si faltan)
- **Ejecutar**: `python <script>.py` (con el venv activo: `source venv/bin/activate`)
- **Linter**: usa `ruff` si está disponible, si no, lo ignoro

## Convenciones de este espacio

- **Comentarios en español** en los scripts (son didácticos, no profesionales)
- **Sin framework de tests** — los scripts se ejecutan y se ven. Si quieres test, avísame y los añadimos.
- **Ficheros sueltos** — cada script es autocontenido. No hay imports entre ellos.
- **Proyectos multi-fichero** — si un ejercicio crece y necesita varios archivos, va dentro de una carpeta con `__init__.py`. Ahí sí se pueden hacer imports entre los módulos de esa carpeta.
- **No uses `pdb` a menos que lo pidas explícitamente.
- **Lecciones** en `lecciones/` (teoría, explicaciones). **Ejercicios** en `ejercicios/` (código para completar).**
