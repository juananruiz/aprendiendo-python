"""
Ejercicio 13 — lambda, map, filter y comprehensions

La idea de este ejercicio: resolver lo MISMO de tres maneras hasta que las
tres te resulten igual de legibles. No es trabajo repetido, es el músculo
que estamos entrenando.

Ejecuta el fichero al terminar: los asserts del final deben pasar.
"""

CANDIDATOS = [
    {"nombre": "Ana",     "nota": 8.5, "cuerpo": "A2", "destino": "Sevilla"},
    {"nombre": "Carlos",  "nota": 4.0, "cuerpo": "C1", "destino": "Cádiz"},
    {"nombre": "Beatriz", "nota": 9.2, "cuerpo": "A2", "destino": "Sevilla"},
    {"nombre": "David",   "nota": 6.1, "cuerpo": "A1", "destino": "Huelva"},
    {"nombre": "Elena",   "nota": 4.9, "cuerpo": "C1", "destino": "Cádiz"},
]


# --- 1. El mismo problema, tres veces -----------------------------------
# Problema: los nombres de los aprobados (nota >= 5), en mayúsculas.

def aprobados_imperativo(candidatos):
    """Con un bucle for y un acumulador. El estilo que ya conoces."""
    # Escribe aquí tu código
    pass


def aprobados_map_filter(candidatos):
    """Con map() y filter() explícitos. Devuelve una lista."""
    # Escribe aquí tu código
    pass


def aprobados_comprehension(candidatos):
    """Con una list comprehension. Una sola línea."""
    # Escribe aquí tu código
    pass


# --- 2. lambda: dónde sí y dónde no -------------------------------------

def ordenar_por_nota(candidatos):
    """
    Devuelve los candidatos ordenados de mayor a menor nota.
    En caso de empate, por nombre alfabético.

    Pista: key=lambda c: (-c["nota"], c["nombre"])
    """
    # Escribe aquí tu código
    pass


def mejor_de_cada_cuerpo(candidatos):
    """
    Devuelve un dict {cuerpo: nombre_del_mejor}.

    Pista: agrupa primero (o usa max() con key sobre una comprehension
    filtrada por cuerpo).
    """
    # Escribe aquí tu código
    pass


# --- 3. Las cuatro familias de comprehension ----------------------------

def notas(candidatos):
    """LISTA con todas las notas."""
    # Escribe aquí tu código
    pass


def indice_por_nombre(candidatos):
    """DICT {nombre: nota}."""
    # Escribe aquí tu código
    pass


def cuerpos_distintos(candidatos):
    """SET con los cuerpos, sin repetir."""
    # Escribe aquí tu código
    pass


def generador_de_nombres(candidatos):
    """
    GENERADOR (paréntesis, no corchetes) con los nombres.
    OJO: no devuelvas una lista. Compruébalo con type().
    """
    # Escribe aquí tu código
    pass


# --- 4. if como filtro vs. if como expresión ----------------------------

def etiquetar(candidatos):
    """
    Lista de strings "Nombre: apto" o "Nombre: no apto" según nota >= 5.
    TODOS los candidatos aparecen. Aquí el if es EXPRESIÓN → va antes del for.
    """
    # Escribe aquí tu código
    pass


def solo_aptos(candidatos):
    """
    Lista de nombres, sólo los que aprueban.
    Aquí el if es FILTRO → va después del for.
    """
    # Escribe aquí tu código
    pass


# --- 5. Anidamiento y aplanado ------------------------------------------

MATRIZ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def aplanar(matriz):
    """[[1,2],[3,4]] -> [1,2,3,4]. Con una comprehension de dos for."""
    # Escribe aquí tu código
    pass


def diagonal(matriz):
    """Los elementos de la diagonal principal. Pista: enumerate()."""
    # Escribe aquí tu código
    pass


def emparejamientos(candidatos, destinos):
    """
    Todos los pares posibles (nombre, destino) — el producto cartesiano
    que hacía inviable la fuerza bruta en la lección 005.
    """
    # Escribe aquí tu código
    pass


# --- 6. La trampa de la pereza ------------------------------------------

def demostrar_pereza():
    """
    Crea un map() sobre [1,2,3] que multiplique por 2.
    SIN convertirlo a lista:
      - imprime el objeto (verás <map object ...>)
      - conviértelo a lista e imprímela
      - conviértelo a lista OTRA VEZ e imprime el resultado

    ¿Qué sale la segunda vez? Anota la respuesta en las preguntas del final.
    """
    # Escribe aquí tu código
    pass


# --- 7. Comprobación -----------------------------------------------------

if __name__ == "__main__":
    esperado = ["ANA", "BEATRIZ", "DAVID"]
    assert aprobados_imperativo(CANDIDATOS) == esperado
    assert aprobados_map_filter(CANDIDATOS) == esperado
    assert aprobados_comprehension(CANDIDATOS) == esperado

    assert [c["nombre"] for c in ordenar_por_nota(CANDIDATOS)] == [
        "Beatriz", "Ana", "David", "Elena", "Carlos"
    ]
    assert mejor_de_cada_cuerpo(CANDIDATOS) == {
        "A2": "Beatriz", "C1": "Elena", "A1": "David"
    }

    assert notas(CANDIDATOS) == [8.5, 4.0, 9.2, 6.1, 4.9]
    assert indice_por_nombre(CANDIDATOS)["Ana"] == 8.5
    assert cuerpos_distintos(CANDIDATOS) == {"A1", "A2", "C1"}

    g = generador_de_nombres(CANDIDATOS)
    assert not isinstance(g, list), "debe ser un generador, no una lista"
    assert next(g) == "Ana"

    assert etiquetar(CANDIDATOS)[0] == "Ana: apto"
    assert etiquetar(CANDIDATOS)[1] == "Carlos: no apto"
    assert len(etiquetar(CANDIDATOS)) == 5, "el ternario no filtra"
    assert solo_aptos(CANDIDATOS) == ["Ana", "Beatriz", "David"]

    assert aplanar(MATRIZ) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert diagonal(MATRIZ) == [1, 5, 9]
    assert len(emparejamientos(CANDIDATOS, ["Sevilla", "Cádiz"])) == 10

    demostrar_pereza()
    print("✅ Las tres notaciones dan lo mismo.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. En demostrar_pereza(), ¿qué sale al convertir el map a lista la
#    SEGUNDA vez? ¿Por qué? ¿Te ha pasado alguna vez sin entenderlo?
# 2. De las tres versiones de aprobados_*, ¿cuál leerías más rápido dentro
#    de seis meses? ¿Y cuál escribirías más rápido hoy?
# 3. mejor_de_cada_cuerpo() probablemente te ha salido fea con
#    comprehensions. Guárdala: en la lección 016 la reescribirás con
#    itertools.groupby y podrás comparar.
# 4. Busca en tus scripts anteriores (orden_burbuja.py, cuadrado_magico.py)
#    un bucle que sea sólo "transformar" o sólo "filtrar". Reescríbelo.
#    ¿Cuántos NO se dejan reescribir, y por qué?
