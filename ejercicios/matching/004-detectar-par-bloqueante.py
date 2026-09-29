"""
Ejercicio 4 — Detectar pares bloqueantes

Dado un matching (asignación) y las preferencias de ambos lados,
determina si el matching es estable o no.

Este es el ejercicio clave para entender qué significa "estabilidad"
antes de implementar Gale-Shapley.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

# --- Preferencias ---

prefs_candidatos = {
    "Ana":     ["Madrid", "Barcelona", "Valencia"],
    "Carlos":  ["Barcelona", "Valencia", "Madrid"],
    "Beatriz": ["Valencia", "Madrid", "Barcelona"],
}

prefs_destinos = {
    "Madrid":    ["Ana", "Beatriz", "Carlos"],
    "Barcelona": ["Carlos", "Ana", "Beatriz"],
    "Valencia":  ["Beatriz", "Ana", "Carlos"],
}


# --- 1. Función auxiliar: ¿quién prefiere qué? ---

def prefieres(preferencias, quien, candidato_a, candidato_b):
    """
    Devuelve True si 'quien' prefiere a 'candidato_a' sobre 'candidato_b'.
    Útil tanto para candidatos como para destinos.
    """
    lista = preferencias[quien]
    # Escribe aquí tu código
    pass


# --- 2. Dado un matching, encontrar el asignado de un destino ---

def obtener_asignados_por_destino(matching):
    """
    matching es un dict {candidato: destino}
    Devuelve un dict inverso {destino: candidato_asignado}
    """
    # Escribe aquí tu código
    pass


# --- 3. Detectar par bloqueante ---

def es_par_bloqueante(prefs_candidatos, prefs_destinos,
                      matching, candidato, destino):
    """
    Devuelve True si 'candidato' y 'destino' formarían un par bloqueante:
    - No están emparejados entre sí
    - El candidato prefiere este destino a su destino actual
    - El destino prefiere a este candidato sobre su asignado actual
    """
    # Escribe aquí tu código
    # Pista: necesitas obtener el destino actual del candidato
    #        y el candidato actual del destino, luego usar prefieres()
    pass


# --- 4. Verificar estabilidad completa ---

def es_matching_estable(prefs_candidatos, prefs_destinos, matching):
    """
    Devuelve True si NO existe ningún par bloqueante en el matching.
    """
    # Escribe aquí tu código
    # Pista: itera sobre todas las combinaciones posibles de
    # candidato y destino que NO están emparejados
    pass


# --- EXTRA: Encontrar todos los pares bloqueantes ---

def encontrar_pares_bloqueantes(prefs_candidatos, prefs_destinos, matching):
    """
    Devuelve una lista de tuplas (candidato, destino) que son pares bloqueantes.
    """
    # Escribe aquí tu código
    pass


# --- Pruebas ---

if __name__ == "__main__":
    matching_estable = {
        "Ana": "Madrid",
        "Carlos": "Barcelona",
        "Beatriz": "Valencia",
    }

    matching_inestable = {
        "Ana": "Barcelona",
        "Carlos": "Madrid",
        "Beatriz": "Valencia",
    }
    # En la lección vimos que Ana y Madrid forman par bloqueante aquí.

    # 1
    assert prefieres(prefs_candidatos, "Ana", "Madrid", "Barcelona") is True
    assert prefieres(prefs_candidatos, "Ana", "Valencia", "Madrid") is False

    # 2
    assert obtener_asignados_por_destino(matching_estable) == {
        "Madrid": "Ana", "Barcelona": "Carlos", "Valencia": "Beatriz",
    }

    # 3
    assert es_par_bloqueante(prefs_candidatos, prefs_destinos,
                              matching_inestable, "Ana", "Madrid") is True
    assert es_par_bloqueante(prefs_candidatos, prefs_destinos,
                              matching_estable, "Ana", "Barcelona") is False, \
        "Ana ya está en su primera opción: no hay destino mejor al que aspirar"

    # 4
    print("Matching estable:", es_matching_estable(prefs_candidatos, prefs_destinos, matching_estable))
    print("Matching inestable:", es_matching_estable(prefs_candidatos, prefs_destinos, matching_inestable))
    assert es_matching_estable(prefs_candidatos, prefs_destinos, matching_estable) is True
    assert es_matching_estable(prefs_candidatos, prefs_destinos, matching_inestable) is False

    # EXTRA
    pares = encontrar_pares_bloqueantes(prefs_candidatos, prefs_destinos, matching_inestable)
    print("Pares bloqueantes en el matching inestable:", pares)
    assert set(pares) == {("Ana", "Madrid"), ("Carlos", "Barcelona")}
    assert encontrar_pares_bloqueantes(prefs_candidatos, prefs_destinos, matching_estable) == []

    print("\n✅ Todo correcto: sabes detectar cuándo un matching es estable y por qué.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---
# 1. ¿Puede haber más de un par bloqueante en el mismo matching?
# 2. ¿Qué ocurre si hay empate en las preferencias?
# 3. Si un matching tiene pares bloqueantes, ¿es siempre posible
#    encontrar otro matching sin ellos?
