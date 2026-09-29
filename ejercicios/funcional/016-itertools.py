"""
Ejercicio 16 — itertools: chain, islice, groupby, product, takewhile

El objetivo no es memorizar el módulo, sino reconocer las formas: "esto es
un groupby", "esto es un product", "esto es un takewhile".

Ejecuta el fichero al terminar: los asserts del final deben pasar.
"""

from itertools import (
    chain,
    combinations,
    count,
    cycle,
    dropwhile,
    groupby,
    islice,
    permutations,
    product,
    takewhile,
)

CANDIDATOS = [
    {"nombre": "Ana",     "cuerpo": "A2", "nota": 8.5},
    {"nombre": "Carlos",  "cuerpo": "C1", "nota": 4.0},
    {"nombre": "Beatriz", "cuerpo": "A2", "nota": 9.2},
    {"nombre": "David",   "cuerpo": "A1", "nota": 6.1},
    {"nombre": "Elena",   "cuerpo": "C1", "nota": 4.9},
    {"nombre": "Fátima",  "cuerpo": "A2", "nota": 7.0},
]


# --- 1. chain: concatenar sin copiar ------------------------------------

def unir_turnos(libre, discapacidad, promocion):
    """
    Devuelve una LISTA con todos los candidatos de los tres turnos,
    en ese orden, usando chain().
    """
    # Escribe aquí tu código
    pass


def aplanar_un_nivel(matriz):
    """
    [[1,2],[3,4],[5,6]] -> [1,2,3,4,5,6], con chain.from_iterable().
    """
    # Escribe aquí tu código
    pass


# --- 2. islice: slicing de lo no indexable ------------------------------

def naturales():
    n = 0
    while True:
        yield n
        n += 1


def primeros(iterable, n):
    """Los n primeros elementos, como lista. Debe aguantar infinitos."""
    # Escribe aquí tu código
    pass


def del_quinto_al_decimo(iterable):
    """Elementos en las posiciones 5,6,7,8,9 (base 0), como lista."""
    # Escribe aquí tu código
    pass


# --- 3. groupby: primero MAL, luego BIEN --------------------------------

def agrupar_mal(candidatos):
    """
    Aplica groupby SIN ordenar antes. Devuelve una lista de tuplas
    (cuerpo, [nombres]).

    Hazlo y mira el resultado: verás cuerpos repetidos. Ese es el punto
    del ejercicio — el fallo es silencioso.
    """
    # Escribe aquí tu código
    pass


def agrupar_bien(candidatos):
    """
    Igual pero ordenando primero por la MISMA key.
    Devuelve un dict {cuerpo: [nombres]}.

    Ojo: los grupos son iteradores perezosos. Materialízalos con list()
    DENTRO de la comprehension, no después.
    """
    # Escribe aquí tu código
    pass


def mejor_de_cada_cuerpo(candidatos):
    """
    Dict {cuerpo: nombre_del_mejor}. Rehaz aquí lo que hiciste a mano en
    el ejercicio 013 y compara cuál se lee mejor.
    """
    # Escribe aquí tu código
    pass


def agrupar_con_defaultdict(candidatos):
    """
    El MISMO resultado que agrupar_bien(), pero con
    collections.defaultdict(list) y un bucle. Impórtalo tú.

    Compara: O(n) frente al O(n log n) de ordenar. ¿Cuál escribirías
    en producción?
    """
    # Escribe aquí tu código
    pass


# --- 4. product y la explosión combinatoria -----------------------------

def emparejamientos(candidatos, plazas):
    """Todos los pares (nombre, plaza) con product()."""
    # Escribe aquí tu código
    pass


def combinaciones_de_bits(n):
    """Todas las tuplas de n bits: product([0,1], repeat=n)."""
    # Escribe aquí tu código
    pass


def cuantos_matchings(n):
    """
    Cuántos emparejamientos completos distintos hay entre n candidatos
    y n plazas. Cuéntalos DE VERDAD con permutations() (no uses
    math.factorial): queremos que notes el coste.

    Con n=9 tarda un rato. Con n=12 no termina. Ese es el ejercicio.
    """
    # Escribe aquí tu código
    pass


def parejas_posibles(nombres):
    """
    Todas las parejas sin repetir y sin importar el orden.
    ¿combinations o permutations? Piénsalo antes de escribir.
    """
    # Escribe aquí tu código
    pass


# --- 5. takewhile / dropwhile vs. filter --------------------------------

NOTAS = [9, 8, 7, 4, 9, 3]


def prefijo_aprobado(notas):
    """Con takewhile: las notas >= 5 desde el principio hasta la 1ª que no."""
    # Escribe aquí tu código
    pass


def desde_el_primer_suspenso(notas):
    """Con dropwhile: todo a partir de la primera nota < 5, incluida."""
    # Escribe aquí tu código
    pass


def todos_los_aprobados(notas):
    """Con filter: todos los >= 5, estén donde estén. Compara los tres."""
    # Escribe aquí tu código
    pass


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_hasta(limite):
    """
    Todos los Fibonacci estrictamente menores que `limite`.
    Con takewhile sobre el generador infinito. Sin contar cuántos son.
    """
    # Escribe aquí tu código
    pass


# --- 6. cycle: reparto round-robin --------------------------------------

def repartir_round_robin(candidatos, tribunales):
    """
    Asigna cada candidato a un tribunal rotando: el 1º al tribunal A,
    el 2º al B, el 3º al C, el 4º otra vez al A...

    Devuelve un dict {tribunal: [nombres]}.
    Pista: cycle() + zip(). zip() se para con el más corto, así que el
    infinito no es problema.
    """
    # Escribe aquí tu código
    pass


# --- 7. Comprobación -----------------------------------------------------

if __name__ == "__main__":
    # 1
    assert unir_turnos(["Ana"], ["Bea"], ["Caro"]) == ["Ana", "Bea", "Caro"]
    assert aplanar_un_nivel([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]

    # 2
    assert primeros(naturales(), 5) == [0, 1, 2, 3, 4]
    assert del_quinto_al_decimo(naturales()) == [5, 6, 7, 8, 9]

    # 3
    mal = agrupar_mal(CANDIDATOS)
    print("   agrupar_mal →", mal)
    assert len(mal) > 3, "sin ordenar salen grupos repetidos: ese es el punto"

    bien = agrupar_bien(CANDIDATOS)
    assert bien == {
        "A1": ["David"],
        "A2": ["Ana", "Beatriz", "Fátima"],
        "C1": ["Carlos", "Elena"],
    }
    assert agrupar_con_defaultdict(CANDIDATOS) == bien
    assert mejor_de_cada_cuerpo(CANDIDATOS) == {
        "A1": "David", "A2": "Beatriz", "C1": "Elena"
    }

    # 4
    assert len(emparejamientos(CANDIDATOS, ["Sevilla", "Cádiz"])) == 12
    assert len(combinaciones_de_bits(3)) == 8
    assert cuantos_matchings(5) == 120
    assert cuantos_matchings(7) == 5040
    assert len(parejas_posibles(["A", "B", "C"])) == 3

    # 5
    assert prefijo_aprobado(NOTAS) == [9, 8, 7]
    assert desde_el_primer_suspenso(NOTAS) == [4, 9, 3]
    assert todos_los_aprobados(NOTAS) == [9, 8, 7, 9]
    assert fibonacci_hasta(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # 6
    reparto = repartir_round_robin(CANDIDATOS, ["A", "B", "C"])
    assert reparto["A"] == ["Ana", "David"]
    assert reparto["B"] == ["Carlos", "Elena"]
    assert reparto["C"] == ["Beatriz", "Fátima"]

    print("✅ Arsenal de iteradores dominado.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. Mira la salida de agrupar_mal(). Si esto pasara con los datos reales
#    de una convocatoria, ¿te darías cuenta? ¿Cómo? (Pista: no lanza error.)
# 2. Cronometra cuantos_matchings(8), (9) y (10) con time.perf_counter().
#    Extrapola: ¿cuánto tardaría con 15 candidatos? ¿Y con 20?
# 3. agrupar_bien() usa sorted+groupby, O(n log n). agrupar_con_defaultdict()
#    es O(n). ¿En qué situación real elegirías groupby de todas formas?
# 4. prefijo_aprobado y todos_los_aprobados dan resultados distintos sobre
#    los mismos datos. ¿En qué caso de negocio querrías cada uno?
# 5. permutations() genera perezosamente, así que la memoria no explota —
#    sólo el tiempo. ¿Cambia eso en algo la conclusión de la lección 005?
