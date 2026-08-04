"""
Ejercicio 2 — Ordenación con key y lambda

Vas a practicar los distintos patrones de ordenación que necesitarás
para implementar Gale-Shapley por tu cuenta.
"""

# --- 1. Ordenar diccionarios por valor ---

puntuaciones = {"Ana": 85, "Carlos": 92, "Beatriz": 78, "David": 92}

# Ordena de mayor a menor puntuación (los empates por orden alfabético)
ranking_ascendente = sorted(puntuaciones.items(),
                            key=lambda x: (-x[1], x[0]))

print("Ranking (nota descendente, nombre ascendente):")
for nombre, nota in ranking_ascendente:
    print(f"  {nombre}: {nota}")


# --- 2. Ordenar lista de dicts por campo anidado ---

candidatos = [
    {"nombre": "Sofía",  "datos": {"nota": 88, "edad": 30}},
    {"nombre": "Miguel", "datos": {"nota": 72, "edad": 25}},
    {"nombre": "Lucía",  "datos": {"nota": 95, "edad": 35}},
    {"nombre": "Jorge",  "datos": {"nota": 65, "edad": 28}},
]

# Ordénalos por nota descendente.
# Escribe aquí tu código:
# candidatos_ordenados = ...


# --- 3. Ranking con índice ---

# Dada una lista ordenada de candidatos, asigna un "puesto"
# (como el ranking de tenis, con empates compartiendo puesto).
# Ejemplo: [(95, 1), (88, 2), (72, 3), (65, 4)]

notas = [95, 88, 95, 72, 65]
nombres = ["Lucía", "Sofía", "Pedro", "Miguel", "Jorge"]

# Combina ambas listas, ordena por nota descendente,
# y asigna puesto con manejo de empates.
# Si dos empatan, ambos tienen el mismo puesto y el siguiente
# se salta los necesarios (ej: 1, 1, 3, 4...)
def asignar_puestos(nombres, notas):
    # Escribe aquí tu código
    pass


# --- 4. Encontrar el mejor candidato para un destino ---

def mejor_candidato_para(destino, preferencias_destino):
    """Devuelve el nombre del candidato más preferido para un destino."""
    # preferencias_destino es un dict {destino: [lista ordenada de candidatos]}
    return preferencias_destino[destino][0] if preferencias_destino[destino] else None


# --- Prueba ---
preferencias_destino = {
    "Madrid": ["Carlos", "Ana", "Beatriz"],
    "Barcelona": ["Ana", "Carlos", "Beatriz"],
}

print("Mejor candidato para Madrid:", mejor_candidato_para("Madrid", preferencias_destino))
# Debería mostrar: "Carlos"


# --- Preguntas de reflexión ---
# 1. ¿Cómo ordenarías si la nota está dentro de un diccionario anidado?
# 2. ¿Qué ventaja tiene usar sorted() frente a .sort() en estos ejercicios?
# 3. ¿Cómo ordenarías múltiples criterios donde unos son ascendentes y otros descendentes?
