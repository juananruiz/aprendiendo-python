# Aprendizaje: Slicing, enumerate y control de bucles

**Fecha**: 2026-06-26
**Lección**: [0001-slicing-enumerate-y-control-de-bucles.html](lecciones/0001-slicing-enumerate-y-control-de-bucles.html)

## Lo aprendido

- **Slicing**: sintaxis `lista[inicio:fin:paso]`, slicing invertido, crear copias
- **enumerate**: obtener índice y valor simultáneamente, evitar `range(len(lista))`
- **for/else**: bloque `else` se ejecuta solo si no hubo `break`
- **break/continue**: control de flujo dentro de bucles

## Observaciones

- El script `orden-burbuja.py` tiene un bug (línea 26): `lista[1]` debería ser `lista[i]`. Esto es un error clásico de índice fijo.
- La búsqueda binaria usa una bandera `numero_encontrado` que podría reemplazarse con `for/else`.
- El slicing crea copias (coste O(n)), importante tenerlo en cuenta para algoritmos.

## Próximos pasos

- Refactorizar `orden-burbuja.py` usando `enumerate` y corrigiendo el bug
- Practicar slicing en la consola interactiva
- Leer capítulo 2 del libro (Selection Sort) para ver bucles anidados en contexto
