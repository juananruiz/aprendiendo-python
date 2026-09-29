"""
Ejercicio 1 — Generar ranking de preferencias

Contexto: tienes un proceso selectivo con 5 candidatos y 3 destinos.
Cada candidato tiene una puntuación numérica y cada destino tiene
una nota de corte. Además, cada candidato tiene preferencias
personales sobre los destinos.

Tu tarea: generar los dos rankings de preferencias (candidatos→destinos
y destinos→candidatos) a partir de los datos brutos.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

# --- Datos de partida ---

candidatos = {
    "Sofía":  {"nota": 88, "preferencia_destinos": ["Madrid", "Bilbao", "Toledo", "Girona"]},
    "Miguel": {"nota": 72, "preferencia_destinos": ["Bilbao", "Girona", "Toledo", "Madrid"]},
    "Lucía":  {"nota": 95, "preferencia_destinos": ["Madrid", "Girona", "Bilbao", "Toledo"]},
    "Jorge":  {"nota": 65, "preferencia_destinos": ["Toledo", "Bilbao", "Madrid", "Girona"]},
    "Elena":  {"nota": 80, "preferencia_destinos": ["Girona", "Madrid", "Toledo", "Bilbao"]},
}

destinos = {
    "Madrid": {"plazas": 2, "nota_minima": 70},
    "Bilbao": {"plazas": 1, "nota_minima": 60},
    "Toledo": {"plazas": 1, "nota_minima": 75},
    "Girona": {"plazas": 1, "nota_minima": 65},
}


def generar_ranking_candidatos(candidatos, destinos):
    """
    Para cada candidato, genera su lista de destinos ordenada por preferencia,
    pero FILTRANDO aquellos cuya nota_minima no alcanza.
    Pista: itera sobre candidatos, filtra por nota >= nota_minima,
           ordena según preferencia_destinos del candidato
    """
    ranking = {}
    for candidato, datos in candidatos.items():
        ranking[candidato] = []
        for destino in datos["preferencia_destinos"]:
            if datos["nota"] >= destinos[destino]["nota_minima"]:
                ranking[candidato].append(destino)
    return ranking


def generar_ranking_destinos(candidatos, destinos):
    """
    Para cada destino, genera una lista de candidatos ordenados
    de mayor a menor nota (los que cumplan la nota mínima).
    """
    ranking = {}
    # Escribe aquí tu código
    return ranking


# --- Pruebas ---

if __name__ == "__main__":
    for candidato, datos in candidatos.items():
        print(candidato, datos["nota"])

    ranking_candidatos = generar_ranking_candidatos(candidatos, destinos)
    ranking_destinos = generar_ranking_destinos(candidatos, destinos)

    print("=== Ranking candidatos → destinos ===")
    for candidato, lista_destinos in ranking_candidatos.items():
        print(f"  {candidato}: {lista_destinos}")

    print("\n=== Ranking destinos → candidatos ===")
    for destino, lista_candidatos in ranking_destinos.items():
        print(f"  {destino}: {lista_candidatos}")

    # --- Verificación ---
    assert ranking_candidatos == {
        "Sofía": ["Madrid", "Bilbao", "Toledo", "Girona"],
        "Miguel": ["Bilbao", "Girona", "Madrid"],
        "Lucía": ["Madrid", "Girona", "Bilbao", "Toledo"],
        "Jorge": ["Bilbao", "Girona"],
        "Elena": ["Girona", "Madrid", "Toledo", "Bilbao"],
    }
    assert ranking_destinos["Madrid"] == ["Lucía", "Sofía", "Elena", "Miguel"], \
        "Madrid pide 70: Jorge (65) se queda fuera; el resto, de mayor a menor nota"
    assert ranking_destinos["Bilbao"] == ["Lucía", "Sofía", "Elena", "Miguel", "Jorge"], \
        "Bilbao pide solo 60: entran los 5 candidatos"
    assert ranking_destinos["Toledo"] == ["Lucía", "Sofía", "Elena"], \
        "Toledo pide 75: Miguel (72) y Jorge (65) se quedan fuera"
    assert ranking_destinos["Girona"] == ["Lucía", "Sofía", "Elena", "Miguel", "Jorge"], \
        "Jorge llega justo a la nota mínima de Girona (65 >= 65)"

    print("\n✅ Todo correcto: los dos rankings respetan la nota mínima y el orden de preferencia/nota.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---
# 1. ¿Qué pasa si un candidato no alcanza la nota mínima de ningún destino?
# 2. ¿Qué pasa si un destino tiene menos candidatos que plazas?
# 3. ¿Cómo romperías un empate si dos candidatos tienen la misma nota?
