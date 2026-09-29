"""
Ejercicio 5 — Fuerza bruta: enumerar todos los matchings posibles

Contexto: en la lección 5 viste que el número de matchings posibles
crece como N! (factorial). Para un caso pequeño (3x3) todavía es viable
generarlos todos y comprobar cuáles son estables. Este ejercicio te lo
demuestra en la práctica, antes de pasar al algoritmo real (que no
necesita fuerza bruta).

Reutiliza las funciones que ya escribiste en el ejercicio 4
(prefieres, es_par_bloqueante, es_matching_estable) — cópialas aquí
o impórtalas si prefieres organizar el código en un módulo.
"""

from itertools import permutations

# --- Preferencias (3x3, para que la fuerza bruta sea manejable) ---

prefs_proponentes = {
    "Alba":   ["Mar", "Nora", "Olga"],
    "Bruno":  ["Mar", "Olga", "Nora"],
    "Cora":   ["Nora", "Mar", "Olga"],
}

prefs_receptores = {
    "Mar":   ["Bruno", "Alba", "Cora"],
    "Nora":  ["Cora", "Alba", "Bruno"],
    "Olga":  ["Alba", "Bruno", "Cora"],
}

proponentes = list(prefs_proponentes.keys())
receptores = list(prefs_receptores.keys())


# --- 1. Funciones de la lección 4 (cópialas y complétalas) ---

def prefieres(preferencias, quien, opcion_a, opcion_b):
    """True si 'quien' prefiere 'opcion_a' sobre 'opcion_b'."""
    # Escribe aquí tu código (o pégalo de tu ejercicio 4 ya resuelto)
    pass


def es_matching_estable(prefs_proponentes, prefs_receptores, matching):
    """
    matching es un dict {proponente: receptor}.
    Devuelve True si NO existe ningún par bloqueante.
    """
    # Escribe aquí tu código (o pégalo de tu ejercicio 4 ya resuelto)
    pass


# --- 2. Generar TODOS los matchings posibles ---

def generar_todos_los_matchings(proponentes, receptores):
    """
    Devuelve una lista de dicts {proponente: receptor}, uno por cada
    matching posible.

    Pista: fija el orden de 'proponentes'. Cada permutación de
    'receptores' (itertools.permutations) te da un matching distinto
    al emparejar posición a posición.
    """
    matchings = []
    # Escribe aquí tu código
    return matchings


# --- 3. Contar y clasificar ---

def contar_matchings_estables(prefs_proponentes, prefs_receptores):
    """
    Genera todos los matchings posibles, cuenta cuántos hay en total
    y cuántos son estables. Devuelve (total, estables, lista_de_estables).
    """
    # Escribe aquí tu código
    pass


# --- Pruebas ---

if __name__ == "__main__":
    total, estables, matchings_estables = contar_matchings_estables(
        prefs_proponentes, prefs_receptores
    )

    print(f"Matchings totales posibles: {total}")
    print(f"Matchings estables: {estables}")
    print()
    print("Los matchings estables son:")
    for m in matchings_estables:
        print(" ", m)

    # --- Verificación ---
    assert total == 6, f"con 3 proponentes y 3 receptores hay 3! = 6 matchings posibles, no {total}"
    assert estables == 1, f"con estas preferencias solo hay un matching estable, no {estables}"
    assert len(matchings_estables) == 1
    assert matchings_estables[0] == {"Alba": "Olga", "Bruno": "Mar", "Cora": "Nora"}, \
        "el matching estable debería ser Alba-Olga · Bruno-Mar · Cora-Nora"

    print("\n✅ Todo correcto: a fuerza bruta, solo 1 de los 6 matchings posibles es estable.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---
# 1. ¿Cuántos matchings totales esperabas para 3 proponentes y 3
#    receptores, antes de ejecutar el código? ¿Coincide con 3! ?
# 2. ¿Cuántos matchings estables encontraste? ¿Es solo uno o hay varios?
# 3. Si aumentas a 4x4 (como en la lección 6), ¿cuántos matchings
#    totales habría? Calcúlalo antes de probarlo y comprueba que
#    itertools.permutations no tarda una eternidad.
# 4. Cambia una sola preferencia en prefs_receptores y vuelve a
#    ejecutar. ¿Cambia el número de matchings estables?
