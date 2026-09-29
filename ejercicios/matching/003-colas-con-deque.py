"""
Ejercicio 3 — Colas con deque: simular la fila de propuestas

En Gale-Shapley, los candidatos libres esperan en una cola. Van
proponiendo uno por uno. Si son rechazados, vuelven a la cola.

Este ejercicio simula esa dinámica a pequeña escala.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
Excepción: la simulación de la sección 2 es aleatoria por diseño (el
propio enunciado dice "rechaza simulado aleatoriamente"), así que no
se verifica con un valor exacto — solo se comprueba que devuelve una
lista. La sección 3 (con prioridad) sí es determinista y se verifica
del todo.
"""

from collections import deque


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
    la prioridad (de mayor a menor nota). Devuelve ese deque, en
    orden de mayor a menor prioridad.
    """
    # Escribe aquí tu código para ordenar candidatos por prioridad
    # y luego meterlos en un deque
    pass


# --- Pruebas ---

if __name__ == "__main__":
    # 1. Operaciones básicas con deque
    cola = deque()
    cola.append("A")
    cola.append("B")
    cola.append("C")

    primero = cola.popleft()
    print("Primero en salir:", primero)
    print("Ahora la cola tiene:", list(cola))
    print("Siguiente sin sacar:", cola[0])

    assert primero == "A", "FIFO: el primero en entrar (append) es el primero en salir (popleft)"
    assert list(cola) == ["B", "C"]
    assert cola[0] == "B"

    # 2. Mini-simulación (aleatoria: solo comprobamos la forma, no el resultado exacto)
    candidatos_ejemplo = ["Ana", "Carlos", "Beatriz", "David"]
    resultado = simular_propuestas(candidatos_ejemplo)
    print("\nAsignados:", resultado)
    assert isinstance(resultado, list), "simular_propuestas debe devolver una lista"

    # 3. Con prioridad (determinista: sí se verifica el resultado exacto)
    prioridad = {"Ana": 80, "Carlos": 95, "Beatriz": 70, "David": 88}
    cola_priorizada = simular_propuestas_priorizadas(candidatos_ejemplo, prioridad)
    print("Cola priorizada (mayor a menor nota):", list(cola_priorizada))
    assert isinstance(cola_priorizada, deque), "usa deque, tal y como pide el enunciado"
    assert list(cola_priorizada) == ["Carlos", "David", "Ana", "Beatriz"]

    print("\n✅ Todo correcto: FIFO con deque y reordenación por prioridad, dominados.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---
# 1. ¿Qué pasa si un candidato es rechazado por todos los destinos?
# 2. ¿Cómo modificarías el código para que cada candidato
#    lleve un contador de a qué destino propuso por última vez?
# 3. ¿Por qué deque es mejor que una lista para esto?
