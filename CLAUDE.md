# Aprendiendo Python — Curso práctico

Este repositorio es un curso práctico de Python en español (ver README.md y
TEMARIO.md). Nació como cuaderno personal y ahora es un recurso abierto: el
contenido público no debe contener referencias personales de ningún alumno.

## Enfoque didáctico

Cuando el usuario pregunte sobre Python, prioriza:

1. **Explicar el concepto** antes que dar el código. Si pregunta "cómo hago X",
   primero responde qué significa X, luego cómo se implementa.
2. **Señalar errores comunes** — off-by-one, mutabilidad, scope, etc. — típicos
   del nivel del script en cuestión.
3. **Darlo hecho o darlo pensado** según el objetivo: si es práctica, pistas;
   si es referencia, la solución completa. Los ejercicios del curso nunca se
   entregan resueltos: son esqueletos con `pass` y `assert`s de verificación.
4. **Verificar antes de afirmar**: si una lección va a incluir cifras o
   comportamientos ("esto es O(n²)", "esto devuelve X"), comprobarlo
   ejecutando código antes de escribirlo.

## Estructura del proyecto

| Carpeta | Contenido |
|---------|-----------|
| `lecciones/fundamentos/` | Módulo 1 — fundamentos (serie 030- y 0001) |
| `lecciones/algoritmos/` | Módulo 2 — el libro de Bhargava (serie 020-) |
| `lecciones/matching/` | Módulo 3 — Gale-Shapley (series 001-010) |
| `lecciones/funcional/` | Módulo 4 — programación funcional (serie 011-018) |
| `lecciones/index.html` | Portada del curso |
| `ejercicios/` | Esqueletos de ejercicio, espejo de los módulos |
| `ejercicios/matematicas/` | Scripts y notebooks matemáticos |
| `referencia/` | Referencia rápida de sintaxis (HTML, 11 fichas + cheatsheet) |
| `algoritmos/` | Scripts de algoritmos clásicos citados por las lecciones |
| `assets/` | Hoja de estilos común (`estilos.css`) e imágenes |
| `herramientas/` | `progreso.py` — seguimiento de progreso en modo texto (ver más abajo) |
| `personal/` | **Solo local, en .gitignore**: MISSION, NOTES, PROGRESO, learning-records del alumno y `progreso.json` |

## Convenciones

- **Todo en español**: lecciones, comentarios, nombres didácticos.
- **Lecciones**: HTML autocontenido que enlaza `assets/estilos.css` (ruta
  relativa `../../assets/` desde los módulos), con barra `nav-lecciones`
  arriba y abajo, y pie que remite a un asistente de IA como profesor.
- **Ejercicios**: docstring de contexto + funciones con pista y `pass` +
  bloque `if __name__ == "__main__"` con `assert`s verificados contra una
  solución de referencia antes de publicarlos.
- **Seguimiento en modo texto**: los ejercicios de fundamentos, algoritmos,
  matching y funcional llaman a `herramientas.progreso.registrar_completado()`
  justo después de confirmar el éxito (tras los `assert`s, o dentro de la
  rama `if` de éxito en los ejercicios que verifican con `if/else` en vez de
  `assert`). Guarda el progreso en `personal/progreso.json` (fuera de git).
  `python -m herramientas.progreso` muestra el resumen (barras de progreso
  en texto, racha, siguiente ejercicio recomendado). Un ejercicio nuevo se
  suma automáticamente al total en cuanto añade esa llamada al terminar su
  bloque `__main__`.
- **Contenido público sin datos personales**: nada de nombres reales,
  empleadores ni biografía en lecciones/ejercicios. El seguimiento personal
  vive en `personal/` (fuera de git). Los nombres de ciudades y personas de
  los ejemplos (Sevilla, Ana, Carlos...) son ficticios y están bien.
- **Al crear una lección**: añadirla a `lecciones/index.html` y al
  `TEMARIO.md`, verificar los enlaces con un script, y compilar el ejercicio
  (`python -m py_compile`).
- **Sin framework de tests** — los `assert`s del propio ejercicio hacen ese
  papel. No usar `pdb` salvo petición explícita.

## Setup técnico

- Python 3.10+ (el venv local del autor está en `venv/`, fuera de git)
- Dependencias solo para scripts sueltos: SymPy, matplotlib, SQLAlchemy, Flet
- Linter: `ruff` si está disponible
