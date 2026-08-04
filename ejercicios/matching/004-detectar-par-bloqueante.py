"""
Ejercicio 4 — Detectar pares bloqueantes

Dado un matching (asignación) y las preferencias de ambos lados,
determina si el matching es estable o no.

Este es el ejercicio clave para entender qué significa "estabilidad"
antes de implementar Gale-Shapley.
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


# --- Pruebas ---

matching_estable = {
    "Ana": "Madrid",
    "Carlos": "Barcelona",
    "Beatriz": "Valencia",
}
# ¿Este matching es estable? Depende de las preferencias.
# Compruébalo con tu función.

matching_inestable = {
    "Ana": "Barcelona",
    "Carlos": "Madrid",
    "Beatriz": "Valencia",
}
# En la lección vimos que Ana y Madrid forman par bloqueante aquí.

print("Matching estable:", es_matching_estable(prefs_candidatos, prefs_destinos, matching_estable))
print("Matching inestable:", es_matching_estable(prefs_candidatos, prefs_destinos, matching_inestable))


# --- EXTRA: Encontrar todos los pares bloqueantes ---

def encontrar_pares_bloqueantes(prefs_candidatos, prefs_destinos, matching):
    """
    Devuelve una lista de tuplas (candidato, destino) que son pares bloqueantes.
    """
    # Escribe aquí tu código
    pass


# --- Preguntas de reflexión ---
# 1. ¿Puede haber más de un par bloqueante en el mismo matching?
# 2. ¿Qué ocurre si hay empate en las preferencias?
# 3. Si un matching tiene pares bloqueantes, ¿es siempre posible
#    encontrar otro matching sin ellos?
