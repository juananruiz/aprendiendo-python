"""
Ejercicio 1 — Generar ranking de preferencias

Contexto: tienes un proceso selectivo con 5 candidatos y 3 destinos.
Cada candidato tiene una puntuación numérica y cada destino tiene
una nota de corte. Además, cada candidato tiene preferencias
personales sobre los destinos.

Tu tarea: generar los dos rankings de preferencias (candidatos→destinos
y destinos→candidatos) a partir de los datos brutos.
"""

from collections import OrderedDict

# --- Datos de partida ---

candidatos = {
    "Sofía":  {"nota": 88, "preferencia_destinos": ["Madrid", "Bilbao", "Toledo", "Girona"]},
    "Miguel": {"nota": 72, "preferencia_destinos": ["Bilbao", "Girona", "Toledo", "Madrid"]},
    "Lucía":  {"nota": 95, "preferencia_destinos": ["Madrid", "Girona", "Bilbao", "Toledo"]},
    "Jorge":  {"nota": 65, "preferencia_destinos": ["Toledo", "Bilbao", "Madrid", "Girona"]},
    "Elena":  {"nota": 80, "preferencia_destinos": ["Girona", "Madrid", "Toledo", "Bilbao"]},
}

for candidato, datos in candidatos.items():
    print(candidato, datos["nota"])

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

ranking_candidatos = generar_ranking_candidatos(candidatos, destinos)
ranking_destinos = generar_ranking_destinos(candidatos, destinos)

print("=== Ranking candidatos → destinos ===")
for candidato, destinos in ranking_candidatos.items():
    print(f"  {candidato}: {destinos}")

# print("\n=== Ranking destinos → candidatos ===")
# for d, cands in ranking_destinos.items():
#     print(f"  {d}: {cands}")


# --- Preguntas de reflexión ---
# 1. ¿Qué pasa si un candidato no alcanza la nota mínima de ningún destino?
# 2. ¿Qué pasa si un destino tiene menos candidatos que plazas?
# 3. ¿Cómo romperías un empate si dos candidatos tienen la misma nota?
