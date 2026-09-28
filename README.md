# Aprendiendo Python

Un curso práctico de Python en español, nacido de un cuaderno de aprendizaje
personal y reorganizado para que cualquiera pueda seguirlo.

**Empieza aquí → [`lecciones/index.html`](lecciones/index.html)** (ábrelo en
tu navegador; funciona en local, sin servidor). El plan completo, incluidas
las partes aún en construcción, está en el [TEMARIO](TEMARIO.md).

## Filosofía

Este curso persigue cuatro objetivos, en este orden de importancia:

1. **Implementar y entender algoritmos clásicos**, siguiendo el libro
   *Comprender los algoritmos* de Aditya Y. Bhargava — no copiando el código,
   sino reescribiéndolo desde cero y midiendo su comportamiento real.
2. **Automatizar tareas del día a día** — Python como herramienta de
   propósito general, deliberadamente lejos del desarrollo web.
3. **Construir una base sólida** de Python idiomático, con criterio para
   elegir la estructura de datos correcta.
4. **Entrenar el pensamiento funcional** — un cambio de aires deliberado
   para quien trabaja a diario en modo OOP.

Y tres no-objetivos igual de importantes: no es un curso de desarrollo web,
ni de machine learning, ni prepara ninguna certificación.

## Cómo funciona

- **Teoría**: cada lección es un HTML autocontenido en `lecciones/`, con
  ejemplos verificados con código real (cuando una lección afirma "esto tarda
  124.750 comparaciones", ese número se midió de verdad).
- **Práctica**: casi toda lección tiene un esqueleto en `ejercicios/` para
  teclear tú — con `assert`s de autoverificación: si pasan, el tema está
  superado. Ningún ejercicio viene resuelto.
- **Consulta**: `referencia/` es una referencia rápida de sintaxis para no
  ir a Google a mitad de ejercicio.
- **Progreso**: cada ejercicio que superas se registra solo (en local) al
  pasar sus `assert`s. Ejecuta `python -m herramientas.progreso` cuando
  quieras para ver tu progreso en texto: barras por módulo, racha de días y
  el siguiente ejercicio recomendado.
- **Un consejo**: usa un asistente de IA como profesor. Pídele que te
  explique un concepto de otra forma, que revise tu solución o que te ponga
  un ejercicio extra — pero teclea tú el código.

## Consultar referencia rápida

La carpeta referencia/ contiene fichas de sintaxis para consultar sin salir del editor.

## Estructura

| Carpeta | Contenido |
|---------|-----------|
| `lecciones/fundamentos/` | Módulo 1 — fundamentos a fondo (bucles, slicing...) |
| `lecciones/algoritmos/` | Módulo 2 — capítulos del libro de Bhargava |
| `lecciones/matching/` | Módulo 3 — proyecto integrador: Gale-Shapley paso a paso |
| `lecciones/funcional/` | Módulo 4 — programación funcional completa |
| `ejercicios/` | Esqueletos de ejercicio, espejo de los módulos de lecciones |
| `referencia/` | Referencia rápida de sintaxis (11 fichas + cheatsheet) |
| `algoritmos/` | Scripts de algoritmos clásicos que las lecciones citan |
| `herramientas/` | `progreso.py` — resumen de progreso en modo texto |
| `TEMARIO.md` | El plan completo del curso, con lo hecho y lo pendiente |

Para tu **seguimiento personal**, copia el TEMARIO a una carpeta `personal/`
(está en el `.gitignore`) y marca ahí tu progreso — el curso es de todos,
tu avance es tuyo. Ahí mismo se guarda automáticamente `progreso.json`, el
registro que lee `herramientas/progreso.py`.

## Requisitos

Python 3.10 o superior. Sin dependencias para casi todo el curso; algunos
scripts sueltos usan SymPy, matplotlib, SQLAlchemy o Flet (se indican en el
propio fichero).

## Instalación

``` shell
# Clonar el repositorio
git clone https://github.com/juananruiz/aprendiendo-python.git
cd aprendiendo-python

# Abrir las lecciones en el navegador
# Abre lecciones/index.html con tu navegador
```

## Recursos adicionales

- Libro de referencia: "Comprender los algoritmos" de Aditya Y. Bhargava
- Cheatsheet de Python incluido (png)
- Documentación oficial de Python 3

## Licencia

[CC BY-SA 4.0](LICENSE.md) — puedes usar, compartir y adaptar este material,
incluso comercialmente, citando la fuente y manteniendo la misma licencia en
las obras derivadas.
