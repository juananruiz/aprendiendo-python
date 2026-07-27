"""
Ejercicio 3 — Colas con deque: simular la fila de propuestas

En Gale-Shapley, los candidatos libres esperan en una cola. Van
proponiendo uno por uno. Si son rechazados, vuelven a la cola.

Este ejercicio simula esa dinámica a pequeña escala.
"""

from collections import deque


# --- 1. Operaciones básicas con deque ---

cola = deque()
cola.append("A")
cola.append("B")
cola.append("C")

print("Primero en salir:", cola.popleft())  # ¿Qué sale?
print("Ahora la cola tiene:", list(cola))
print("Siguiente sin sacar:", cola[0])


# --- 2. Simular una ronda de propuestas ---

def simular_propuestas(candidatos):
    """
    candidatos: lista de nombres
    Simula que cada candidato propone a su 'siguiente destino'.
    Si el destino lo rechaza (simulado aleatoriamente), vuelve
    a la cola. Si lo acepta, sale de la cola.

    Implementa la lógica para que se repita hasta que todos
    estén asignados o no queden destinos.
    """
    pendientes = deque(candidatos)
    asignados = []
    # Necesitamos algún "destino" simulado para rechazar/aceptar
    destinos_disponibles = {"Madrid": 2, "Bilbao": 1, "Toledo": 1}

    # Escribe aquí el bucle principal:
    # Mientras haya pendientes y destinos disponibles,
    # saca un candidato, intenta asignarlo a un destino,
    # si el destino tiene plazas, se asigna; si no, vuelve a la cola.
    return asignados


# --- 3. Simular con orden de prioridad ---

def simular_propuestas_priorizadas(candidatos, prioridad):
    """
    candidatos: lista de nombres
    prioridad: dict {nombre: nota} para ordenar quién propone primero

    Usa deque como cola pero REORDENA antes de empezar según
    la prioridad (de mayor a menor nota).
    """
    # Escribe aquí tu código para ordenar candidatos por prioridad
    # y luego meterlos en un deque
    pass


# --- 4. Mini-simulación para probar ---

candidatos_ejemplo = ["Ana", "Carlos", "Beatriz", "David"]
resultado = simular_propuestas(candidatos_ejemplo)
print("Asignados:", resultado)


# --- Preguntas de reflexión ---
# 1. ¿Qué pasa si un candidato es rechazado por todos los destinos?
# 2. ¿Cómo modificarías el código para que cada candidato
#    lleve un contador de a qué destino propuso por última vez?
# 3. ¿Por qué deque es mejor que una lista para esto?
