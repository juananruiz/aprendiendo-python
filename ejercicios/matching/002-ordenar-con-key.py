"""
Ejercicio 2 — Ordenación con key y lambda

Vas a practicar los distintos patrones de ordenación que necesitarás
para implementar Gale-Shapley por tu cuenta.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

# --- 1. Ordenar diccionarios por valor ---

puntuaciones = {"Ana": 85, "Carlos": 92, "Beatriz": 78, "David": 92}


# --- 2. Ordenar lista de dicts por campo anidado ---

candidatos = [
    {"nombre": "Sofía",  "datos": {"nota": 88, "edad": 30}},
    {"nombre": "Miguel", "datos": {"nota": 72, "edad": 25}},
    {"nombre": "Lucía",  "datos": {"nota": 95, "edad": 35}},
    {"nombre": "Jorge",  "datos": {"nota": 65, "edad": 28}},
]


# --- 3. Ranking con índice ---

notas = [95, 88, 95, 72, 65]
nombres = ["Lucía", "Sofía", "Pedro", "Miguel", "Jorge"]


def asignar_puestos(nombres, notas):
    """
    Combina ambas listas, ordena por nota descendente, y asigna un
    "puesto" (como el ranking de tenis, con empates compartiendo
    puesto y el siguiente saltándose los que hagan falta: 1, 1, 3, 4...).

    Devuelve una lista de tuplas (nombre, puesto), en el orden que
    queda tras ordenar por nota.

    asignar_puestos(["Lucía","Sofía","Pedro","Miguel","Jorge"], [95,88,95,72,65])
        -> [("Lucía", 1), ("Pedro", 1), ("Sofía", 3), ("Miguel", 4), ("Jorge", 5)]
    """
    # Escribe aquí tu código
    pass


# --- 4. Encontrar el mejor candidato para un destino ---

def mejor_candidato_para(destino, preferencias_destino):
    """Devuelve el nombre del candidato más preferido para un destino."""
    # preferencias_destino es un dict {destino: [lista ordenada de candidatos]}
    return preferencias_destino[destino][0] if preferencias_destino[destino] else None


preferencias_destino = {
    "Madrid": ["Carlos", "Ana", "Beatriz"],
    "Barcelona": ["Ana", "Carlos", "Beatriz"],
}


# --- Pruebas ---

if __name__ == "__main__":
    # 1
    ranking_ascendente = sorted(puntuaciones.items(),
                                key=lambda x: (-x[1], x[0]))
    print("Ranking (nota descendente, nombre ascendente):")
    for nombre, nota in ranking_ascendente:
        print(f"  {nombre}: {nota}")
    assert ranking_ascendente == [("Carlos", 92), ("David", 92), ("Ana", 85), ("Beatriz", 78)], \
        "Carlos y David empatan a 92: se rompe el empate por nombre ascendente"

    # 2: Ordénalos por nota descendente.
    # Escribe aquí tu código:
    # candidatos_ordenados = ...
    print("\nCandidatos por nota:", [c["nombre"] for c in candidatos_ordenados])
    assert [c["nombre"] for c in candidatos_ordenados] == ["Lucía", "Sofía", "Miguel", "Jorge"]

    # 3
    puestos = asignar_puestos(nombres, notas)
    print("\nPuestos:", puestos)
    assert puestos == [("Lucía", 1), ("Pedro", 1), ("Sofía", 3), ("Miguel", 4), ("Jorge", 5)]

    # 4
    mejor = mejor_candidato_para("Madrid", preferencias_destino)
    print("\nMejor candidato para Madrid:", mejor)
    assert mejor == "Carlos"

    print("\n✅ Todo correcto: dominas los patrones de ordenación con key y lambda.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---
# 1. ¿Cómo ordenarías si la nota está dentro de un diccionario anidado?
# 2. ¿Qué ventaja tiene usar sorted() frente a .sort() en estos ejercicios?
# 3. ¿Cómo ordenarías múltiples criterios donde unos son ascendentes y otros descendentes?
