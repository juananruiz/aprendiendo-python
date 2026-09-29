"""
Ejercicio 7 — Verificar los teoremas con código

Contexto: en la lección 7 demostraste (con lápiz) que el algoritmo de
Gale-Shapley da un matching estable, y que además es proponente-óptimo y
receptor-pésimo. Aquí lo COMPROBARÁS empíricamente, sin haber programado
todavía el algoritmo completo (eso es la lección 8).

La estrategia: reutilizar la fuerza bruta del ejercicio 5 para generar
TODOS los matchings estables de un caso pequeño, y a partir de ahí:

    1. Encontrar todos los pares bloqueantes de un matching cualquiera.
    2. Construir el matching proponente-óptimo y ver que es estable.
    3. Construir el receptor-pésimo y ver que es EL MISMO.

El caso de abajo (3x3) tiene a propósito DOS matchings estables, para que
la diferencia entre "óptimo" y "pésimo" se note.
"""

from itertools import permutations

# --- Caso con DOS matchings estables ---

prefs_proponentes = {
    "A": ["X", "Y", "Z"],
    "B": ["Y", "X", "Z"],
    "C": ["X", "Y", "Z"],
}

prefs_receptores = {
    "X": ["B", "A", "C"],
    "Y": ["A", "B", "C"],
    "Z": ["A", "B", "C"],
}

proponentes = list(prefs_proponentes)
receptores = list(prefs_receptores)


# --- 1. ¿Prefiere X a A sobre B? (de la lección 4) ---

def prefiere(preferencias, quien, opcion_a, opcion_b):
    """
    True si 'quien' prefiere 'opcion_a' sobre 'opcion_b'.

    Pista: en una lista de preferencias, "mejor" = aparece ANTES,
    es decir, tiene un índice más pequeño. Usa .index().
    """
    # Escribe aquí tu código
    pass


# --- 2. TODOS los pares bloqueantes de un matching ---

def parejas_bloqueantes(pp, pr, matching):
    """
    matching : dict {proponente: receptor}
    Devuelve la LISTA de todos los pares (proponente, receptor) que
    bloquean el matching. Lista vacía => el matching es estable.

    Un par (p, r) bloquea si:
      - p NO está emparejado con r, y
      - p prefiere r sobre su pareja actual matching[p], y
      - r prefiere p sobre su pareja actual.

    Pista: necesitas saber, para cada receptor r, con quién está
    emparejado. Como matching va {proponente: receptor}, constrúyete el
    inverso {receptor: proponente}. Luego recorre cada proponente p y
    cada receptor r distinto de su pareja.
    """
    # Escribe aquí tu código
    pass


# --- 3. Generar todos los matchings estables (fuerza bruta del ej. 5) ---

def todos_los_matchings_estables(pp, pr):
    """
    Devuelve la lista de todos los matchings estables (cada uno un dict
    {proponente: receptor}).

    Pista: por cada permutación de 'receptores', empareja posición a
    posición con 'proponentes' para formar un matching, y quédatelo solo
    si parejas_bloqueantes(...) devuelve lista vacía.
    """
    # Escribe aquí tu código
    pass


# --- 4. Matching proponente-óptimo ---

def matching_proponente_optimo(estables, pp):
    """
    A partir de la lista de matchings estables, construye el matching que
    da a CADA proponente su MEJOR pareja válida (la que más prefiere de
    entre todas las que le tocan en algún matching estable).

    Devuelve un dict {proponente: receptor}.

    Pista para cada proponente p:
      - reúne el conjunto de parejas válidas: {m[p] for m in estables}
      - elige la mejor según prefs_proponentes[p] (índice más pequeño)
    """
    # Escribe aquí tu código
    pass


# --- 5. Matching receptor-pésimo ---

def matching_receptor_pesimo(estables, pr):
    """
    Construye el matching que da a CADA receptor su PEOR pareja válida.
    Devuelve un dict {proponente: receptor} (mismo formato que los demás).

    Pista: para cada receptor r, sus parejas válidas son los proponentes
    con los que aparece en algún matching estable. La "peor" es la de
    índice más GRANDE en prefs_receptores[r]. Ojo al formato de salida:
    tendrás que darle la vuelta para devolver {proponente: receptor}.
    """
    # Escribe aquí tu código
    pass


# --- Pruebas ---

if __name__ == "__main__":
    estables = todos_los_matchings_estables(prefs_proponentes, prefs_receptores)

    print(f"Matchings estables encontrados: {len(estables)}")
    for m in estables:
        print("  ", m)

    optimo = matching_proponente_optimo(estables, prefs_proponentes)
    pesimo = matching_receptor_pesimo(estables, prefs_receptores)

    print("\nProponente-óptimo:", optimo)
    print("Receptor-pésimo:  ", pesimo)

    # Garantía 3: el óptimo no tiene pares bloqueantes
    ok_estable = parejas_bloqueantes(prefs_proponentes, prefs_receptores, optimo) == []
    # Garantía 4: proponente-óptimo == receptor-pésimo
    ok_optimalidad = optimo == pesimo

    print()
    print("✅ El proponente-óptimo es estable" if ok_estable
          else "❌ El proponente-óptimo NO es estable — revisa tu código")
    print("✅ Proponente-óptimo == Receptor-pésimo (Garantía 4)" if ok_optimalidad
          else "❌ No coinciden — revisa tu código")

    if ok_estable and ok_optimalidad:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
        from herramientas.progreso import registrar_completado
        registrar_completado(__file__)


# --- Preguntas de reflexión ---
# 1. ¿Cuántos matchings estables salieron? ¿Coincide con lo que esperabas
#    al mirar las preferencias a ojo?
# 2. Compara el proponente-óptimo con el otro matching estable. ¿Quién sale
#    ganando en cada uno? ¿Se ve la "ventaja de proponer"?
# 3. Cambia las preferencias para que solo haya UN matching estable. ¿Qué
#    ocurre entonces con óptimo y pésimo? ¿Por qué?
