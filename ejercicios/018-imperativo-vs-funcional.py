"""
Ejercicio 18 — PROYECTO INSIGNIA de la Pista 4
Contraste imperativo vs. funcional

Tres partes, tal como las pide el ROADMAP:

  A) Reescribir dos algoritmos ya hechos en estilo funcional puro
  B) Montar un pipeline de datos sin variables mutables intermedias
  C) Escribir la reflexión — la parte más importante

Regla del juego para la parte A: prohibido `for` y `while` explícitos,
prohibido mutar. Permitido: comprehensions, map/filter/reduce, recursión,
itertools, functools.

Aviso honesto: algunas de estas reescrituras van a quedar PEOR que el
original. Eso no es un fallo del ejercicio — es el ejercicio.
"""

from functools import reduce
from itertools import chain, groupby, islice
from pathlib import Path

RUTA_DATOS = Path(__file__).parent / "_datos_018.csv"


# ========================================================================
# PARTE A — Reescritura funcional
# ========================================================================

# --- A1. Ordenamiento burbuja -------------------------------------------

def burbuja_imperativa(lista):
    """El original de algoritmos/orden_burbuja.py, para comparar."""
    xs = list(lista)
    n = len(xs)
    for i in range(n):
        for j in range(n - i - 1):
            if xs[j] > xs[j + 1]:
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
    return xs


def una_pasada(lista):
    """
    Una sola pasada de burbuja, PURA: devuelve una lista NUEVA en la que
    cada par adyacente desordenado ha sido intercambiado.

    Sin bucles explícitos y sin mutar la entrada.

    Pista: piénsalo recursivamente sobre la cabeza y la cola.
        - lista de 0 o 1 elementos -> ya está
        - si a > b: b va delante y sigues con [a, *resto]
        - si no:    a va delante y sigues con [b, *resto]
    """
    # Escribe aquí tu código
    pass


def burbuja_funcional(lista):
    """
    Aplica una_pasada() repetidamente hasta que el resultado no cambie.
    Sin while. Sin mutación.

    Pista: recursión — si una_pasada(l) == l, ya está ordenada.
    """
    # Escribe aquí tu código
    pass


# --- A2. Búsqueda binaria -----------------------------------------------

def binaria_imperativa(lista, objetivo):
    """El original de algoritmos/busqueda_binaria_01.py, para comparar."""
    bajo, alto = 0, len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1


def binaria_funcional(lista, objetivo, bajo=0, alto=None):
    """
    La misma búsqueda, recursiva y sin mutar `bajo`/`alto`: se pasan
    como argumentos en cada llamada.

    Devuelve el índice o -1.

    Pista: `alto = len(lista) - 1 if alto is None else alto`
    (¿por qué None y no len(lista)-1 como valor por defecto? Lección 011.)
    """
    # Escribe aquí tu código
    pass


# --- A3. Cuadrado mágico ------------------------------------------------

def es_cuadrado_magico(matriz):
    """
    True si todas las filas, todas las columnas y las dos diagonales
    suman lo mismo.

    Sin un solo bucle explícito. Pista: zip(*matriz) transpone.
    """
    # Escribe aquí tu código
    pass


# --- A4. Factorial y suma -----------------------------------------------

def factorial_funcional(n):
    """Factorial con reduce. Sin recursión y sin bucle."""
    # Escribe aquí tu código
    pass


def suma_digitos(n):
    """
    Suma de los dígitos de un entero. Sin bucle.
    Pista: map(int, str(n))
    """
    # Escribe aquí tu código
    pass


# ========================================================================
# PARTE B — Pipeline de datos
# ========================================================================

def preparar_datos():
    """Ya está hecho. Genera un CSV con ruido realista."""
    filas = [
        "# convocatoria 2026 - datos brutos",
        "nombre;cuerpo;experiencia;formacion;idiomas",
        "  Ana Ruiz  ;A2;8.0;6.0;10.0",
        "Carlos Pérez;C1;4.0;5.0;3.0",
        "",
        "# segundo bloque",
        "BEATRIZ LÓPEZ;A2;9.0;9.5;8.0",
        "david moreno;A1;6.0;7.0;5.0",
        "Elena Gil;C1;5.0;4.0;5.0",
        "Fátima Sanz;A2;7.0;8.0;6.0",
        "registro corrupto sin campos suficientes",
        "Gonzalo Ríos;A1;3.0;2.0;4.0",
    ]
    RUTA_DATOS.write_text("\n".join(filas) + "\n", encoding="utf-8")


# El pipeline: cada etapa es una función pura de iterable a iterable.
# Ninguna acumula en una variable mutable. Ninguna imprime.

def leer(ruta):
    """Generador de líneas sin el salto de línea final."""
    # Escribe aquí tu código
    pass


def quitar_ruido(lineas):
    """Deja pasar las líneas que no están vacías ni empiezan por '#'."""
    # Escribe aquí tu código
    pass


def quitar_cabecera(lineas):
    """
    Salta la primera línea que quede (la de nombres de columna).
    Pista: islice(lineas, 1, None)
    """
    # Escribe aquí tu código
    pass


def a_registros(lineas):
    """
    Convierte "Nombre;CUERPO;8.0;6.0;10.0" en un dict:
        {"nombre": ..., "cuerpo": ..., "experiencia": 8.0,
         "formacion": 6.0, "idiomas": 10.0}

    Las líneas que no tengan 5 campos se DESCARTAN silenciosamente
    (hay una corrupta a propósito). El nombre se normaliza:
    sin espacios sobrantes y en formato Título.
    """
    # Escribe aquí tu código
    pass


def con_baremo(registros, pesos):
    """
    Añade la clave "nota" a cada registro, SIN mutar el original.
    pesos es un dict {"experiencia": 0.5, "formacion": 0.3, "idiomas": 0.2}
    Redondea a 2 decimales.

    Pista: {**r, "nota": ...}
    """
    # Escribe aquí tu código
    pass


def procesar(ruta, pesos):
    """
    Encadena las cinco etapas y devuelve una LISTA de registros
    ordenada de mayor a menor nota.

    Escríbelo como una sola expresión encadenada. Sin variables
    intermedias.
    """
    # Escribe aquí tu código
    pass


def resumen_por_cuerpo(registros):
    """
    Devuelve {cuerpo: nota_media_redondeada_a_2}.
    Con sorted + groupby (acuérdate de la regla de oro de la 016).
    """
    # Escribe aquí tu código
    pass


def informe(registros):
    """
    Lista de strings "Nombre (CUERPO): 7.8", una por registro.
    PURA: no imprime nada. El print() vive sólo en main().
    """
    # Escribe aquí tu código
    pass


# ========================================================================
# Comprobación
# ========================================================================

if __name__ == "__main__":
    import random

    # --- Parte A ---
    for _ in range(20):
        muestra = random.sample(range(100), 10)
        assert burbuja_funcional(muestra) == sorted(muestra)
        assert burbuja_funcional(muestra) == burbuja_imperativa(muestra)
        original = list(muestra)
        burbuja_funcional(muestra)
        assert muestra == original, "burbuja_funcional no debe mutar"

    assert burbuja_funcional([]) == []
    assert burbuja_funcional([1]) == [1]

    ordenada = list(range(0, 200, 2))
    for objetivo in (0, 98, 198, 7, -1):
        assert binaria_funcional(ordenada, objetivo) == binaria_imperativa(
            ordenada, objetivo
        ), f"discrepancia con {objetivo}"

    assert es_cuadrado_magico([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) is True
    assert es_cuadrado_magico([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) is False

    assert factorial_funcional(0) == 1
    assert factorial_funcional(5) == 120
    assert suma_digitos(9875) == 29

    # --- Parte B ---
    preparar_datos()
    PESOS = {"experiencia": 0.5, "formacion": 0.3, "idiomas": 0.2}
    registros = procesar(RUTA_DATOS, PESOS)

    assert len(registros) == 7, "la línea corrupta debe descartarse"
    assert registros[0]["nombre"] == "Beatriz López"
    assert registros[0]["nota"] == 8.95
    assert registros[-1]["nombre"] == "Gonzalo Ríos"
    assert all(
        registros[i]["nota"] >= registros[i + 1]["nota"]
        for i in range(len(registros) - 1)
    ), "debe estar ordenado descendente"

    medias = resumen_por_cuerpo(registros)
    assert set(medias) == {"A1", "A2", "C1"}
    assert medias["A2"] == 7.95  # (7.8 + 8.95 + 7.1) / 3

    for linea in informe(registros):
        print("  ", linea)

    RUTA_DATOS.unlink()
    print("✅ Proyecto insignia de la Pista 4 completado.")


# ========================================================================
# PARTE C — La reflexión (esta parte no la comprueba ningún assert)
# ========================================================================
#
# Rellena esto DESPUÉS de haber hecho A y B. Escribe de verdad, con
# ejemplos concretos de tu propio código de arriba. Es el entregable
# real de la Pista 4: el objetivo era criterio, no dogma.
#
# 1. ¿Cuál de las reescrituras funcionales quedó MEJOR que el original?
#    ¿Por qué exactamente? ¿Legibilidad, menos estado, más testeable?
#
#    ...
#
# 2. ¿Cuál quedó PEOR? Sé específico: ¿fue por rendimiento (la burbuja
#    recursiva es O(n²) en pasadas y O(n) en pila), por legibilidad, o
#    porque Python no está diseñado para eso (límite de recursión)?
#
#    ...
#
# 3. binaria_funcional() es recursiva. Pruébala con una lista de 10
#    millones de elementos. ¿Funciona? ¿Y burbuja_funcional() con 1000?
#    ¿Qué te dice eso sobre la recursión como sustituto del bucle EN
#    PYTHON concretamente? (busca: "tail call optimization python")
#
#    ...
#
# 4. El pipeline de la parte B, ¿te salió más claro o más oscuro que el
#    equivalente con un for y unos ifs? ¿Cambiaría tu respuesta si el
#    fichero tuviera 10 millones de líneas?
#
#    ...
#
# 5. Vuelves el lunes a tu trabajo con PHP y OOP. Nombra TRES cosas
#    concretas de esta pista que vas a usar allí, y una que no.
#
#    ...
#
# 6. Si tuvieras que explicarle a alguien en una frase cuándo elegir
#    estilo funcional y cuándo no, ¿qué frase sería?
#
#    ...
